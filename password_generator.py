import random
import string

choice_uppercase = input("Did you waant to use uppercase letters in password? yes/no :")
choice_lowercase = input("Did you waant to use lowercase letters in password? yes/no :")
choice_specialchar = input("Did you waant to use special characters  in password? yes/no :")
choice_digits = input("Did you waant to use digits in password? yes/no :")
pass_length = int(input("enter the length of password :"))
pass_set=""


if(choice_uppercase.lower() == "yes"):
    pass_set += string.ascii_uppercase
if(choice_lowercase.lower() == "yes"):
    pass_set += string.ascii_lowercase
if(choice_specialchar.lower() == "yes"):
    pass_set += string.punctuation
if(choice_digits.lower() == "yes"):
    pass_set += string.digits

password = "".join([random.choice(pass_set) for i in range(pass_length)])
print("The random password is:",password)