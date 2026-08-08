import json
import random
import string
from pathlib import Path

class Bank:
    database='data.json'
    data=[]
    #database connection
    try:
        if Path(database).exists():
            with open(database) as f:
                data=json.load(f.read())
        else:
            print("Database file not found. Starting with an empty database.")
    except Exception as e:
        print(f"Error loading data: {e}")
    
    #create account
    def create_account(self):
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