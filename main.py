import json
import random
import string
from pathlib import Path

class Bank:
    pass


user = Bank()
print("Press 1 for creating an account:- ")
print("Press 2 for deposit the money:- ")
print("Press 3 for withdraw the money:- ")
print("Press 4 for details of account:- ")
print("Press 5 for update the details:- ")
print("Press 6 for delete the account:- ")


check = int(input("Enter your choice:- "))

if check == 1:
    user.create_account()