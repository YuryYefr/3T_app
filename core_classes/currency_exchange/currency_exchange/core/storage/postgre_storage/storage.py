"""
doc string goes here
"""

__all__ = ['PostgreSQLStorage']

# Standard library imports.
import psycopg2
import itertools
import decimal

# Related third party imports.

# Local application/library specific imports.
from core_classes.currency_exchange.currency_exchange.core.storage import BaseStorage
from core_classes.currency_exchange.currency_exchange.core.storage.python_storage \
    import CurrencyExchangeRate, CurrencyEntity
from .migration import MIGRATION_SCRIPT


class PostgreSQLStorage(BaseStorage):
    _connection = None

    def __init__(self, dbname='', user='', password='', host='127.0.0.1', port=5432, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.connection_params = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }

    @property
    def connection(self):
        if self._connection is None:
            self._connection = psycopg2.connect(**self.connection_params)
        return self._connection

    def store_currencies(self, currencies):
        assert all([isinstance(obj, CurrencyEntity) for obj in currencies])
        conn = self.connection

        currency_codes = [c.get_code() for c in currencies]
        read_sql = 'select code from currency where code in %s;'

        try:
            with conn.cursor() as cursor:
                query_data = tuple(set(currency_codes))
                cursor.execute(read_sql, (query_data,))
                in_db_codes = cursor.fetchall()
        except Exception as e:
            conn.rollback()
            raise e

        in_db_codes = [e[0] for e in in_db_codes]
        diff = set(currency_codes).difference(set(in_db_codes))

        if not diff:
            return

        new_currencies = filter(lambda c: c.get_code() in diff, currencies)
        new_currencies = map(lambda c: (c.get_code(), c.get_name()), new_currencies)

        insert_sql = 'insert into currency (code, name) values (%s, %s);'

        try:
            with conn.cursor() as cursor:
                data_to_insert = tuple(set(new_currencies))
                cursor.executemany(insert_sql, data_to_insert)
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e

    def _store_new_providers(self, providers):
        conn = self.connection

        read_sql = 'select code from provider where code in %s;'

        try:
            with conn.cursor() as cursor:
                query_data = tuple(set(providers))
                cursor.execute(read_sql, (query_data, ))
                in_db_providers = cursor.fetchall()
        except Exception as e:
            conn.rollback()
            raise e

        in_db_providers = [p[0] for p in in_db_providers]
        diff = set(providers).difference(set(in_db_providers))

        if not diff:
            return

        new_providers = filter(lambda p: p in diff, set(providers))
        new_providers = map(lambda p: (p, p), new_providers)

        if new_providers:
            insert_sql = 'insert into provider (code, name) values (%s, %s);'

            try:
                with conn.cursor() as cursor:
                    data_for_insert = tuple(set(new_providers))
                    cursor.executemany(insert_sql, data_for_insert)
                    conn.commit()
            except Exception as e:
                conn.rollback()
                raise e

    def store_rates(self, exchange_rates):
        assert all([isinstance(obj, CurrencyExchangeRate) for obj in exchange_rates])

        if not exchange_rates:
            return

        conn = self.connection

        providers = [r.get_provider() for r in exchange_rates]
        self._store_new_providers(providers)

        currencies = [r.get_from_currency() for r in exchange_rates]
        currencies.extend([r.get_to_currency() for r in exchange_rates])
        self.store_currencies(currencies)

        insert_sql = 'insert into currency_exchange_rate (from_currency_id, to_currency_id, on_date, provider_id, rate) values (%s, %s, %s, %s, %s);'
        data = map(lambda r: (r.get_from_currency().get_code(), r.get_to_currency().get_code(),
                              r.get_on_date(), r.get_provider(), float(r.get_rate())), exchange_rates)

        try:
            with conn.cursor() as cursor:
                data_to_insert = tuple(set(data))
                cursor.executemany(insert_sql, data_to_insert)
                conn.commit()
        except Exception as e:
            conn.rollback()
            raise e

    def get_currencies(self, provider_names, currency_codes):
        result = []
        conn = self.connection

        read_sql = 'select code, name from currency where code in %s;'

        try:
            with conn.cursor() as cursor:
                cursor.execute(read_sql, (tuple(currency_codes), ))
                data = cursor.fetchall()
        except Exception as e:
            conn.rollback()
            raise e

        for val in data:
            currency = CurrencyEntity(val[0], val[1])
            result.append(currency)

        retrieved_codes = [c.get_code() for c in result]
        diff = set(currency_codes).difference(set(retrieved_codes))

        for val in diff:
            result.append(CurrencyEntity(val, val))

        return result

    def get_rates(self, provider_names, currency_code, to_currencies=None, on_date=None):
        conn = self.connection

        currencies = self.get_currencies(None, [currency_code] + (to_currencies or None))
        currencies = {c.get_code(): c for c in currencies}

        def map_query_data(record):
            mapped = record[0] + (record[1], )
            return mapped

        filter_sql = 'provider_id=%s and from_currency_id=%s'

        query_data = itertools.product(provider_names, [currency_code])
        if to_currencies:
            query_data = itertools.product(query_data, to_currencies)
            query_data = map(map_query_data, query_data)
            filter_sql += ' and to_currency_id=%s'

        if on_date:
            query_data = itertools.product(query_data, [on_date])
            query_data = map(map_query_data, query_data)
            filter_sql += ' and on_date=%s'

        query_data = list(query_data)

        filter_sql = '({}) or '.format(filter_sql) * len(query_data)
        filter_sql = filter_sql[:-4]
        query_sql = 'select provider_id, from_currency_id, to_currency_id, rate, on_date ' \
                    'from currency_exchange_rate where {};'.format(filter_sql)

        q_data = []
        for qd in query_data:
            q_data.extend(list(qd))

        try:
            with conn.cursor() as cursor:
                cursor.execute(query_sql, q_data)
                data = cursor.fetchall()
        except Exception as e:
            conn.rollback()
            raise e

        result = list()
        for rec in data:
            tmp = CurrencyExchangeRate(
                rec[0],
                currencies.get(rec[1]),
                currencies.get(rec[2]),
                decimal.Decimal(rec[3]),
                rec[4]
            )
            result.append(tmp)

        return result

    def migrate(self):
        conn = self.connection

        try:
            with conn.cursor() as cursor:
                cursor.execute(MIGRATION_SCRIPT)
                conn.commit()
            return True, None
        except Exception as e:
            conn.rollback()
            return False, str(e)
    
    def drop_tables(self):
        conn = self.connection

        try:
            with conn.cursor() as cursor:
                for table in self.DB_TABLES:
                    cursor.execute('drop table {};'.format(table))
                    conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
