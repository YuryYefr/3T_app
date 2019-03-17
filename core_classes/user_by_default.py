#TBA
import uuid
user_id = uuid.uuid4()
user_name = input("what is your name?: ")
while user_name.isdigit():
    print("no robots allowed")
    user_name = input("what is your name?:")
user_surname = input("what is your surname?: ")
while user_surname.isdigit():
    print("any robots in your family? surname in letters")
    user_surname = input("what is your surname?: ")
admin = "yuriyefr".capitalize()
contact_num = input("your number is?:").strip(str(10))
while contact_num.isalpha():
    print("we need numbers")
    contact_num = input("your number is?:").strip(str(10))
user_email = input("your email: ")

