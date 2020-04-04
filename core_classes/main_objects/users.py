import uuid
admin = "yuriyefr".capitalize()



class UserName:
    user_id = None
    user_name = None
    user_surname = None
    contact_num = None
    user_email = None

    def __init__(self):
        pass

    def __str__(self):
        return f'id{self.user_id}\n name{self.user_name}\n surname{self.user_name}\n ' \
            f'tel num{self.contact_num}\n email{self.user_email}'

    def user_create(self):
        self.user_id = uuid.uuid4()
        self.user_name = input("what is your name?: ").capitalize()
        while self.user_name.isdigit():
            print("no robots allowed")
            self.user_name = input("what is your name?:").capitalize()
        self.user_surname = input("what is your surname?: ").capitalize()
        while self.user_surname.isdigit():
            print("any robots in your family? surname in letters")
            self.user_surname = input("what is your surname?: ")
        self.contact_num = input("your number is?:").strip(str(10))
        while self.contact_num.isalpha():
            print("we need numbers")
            self.contact_num = input("your number is?:").strip(str(10))
        self.user_email = input("your email: ")
        return self
