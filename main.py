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
    
    
    #update database
    @staticmethod
    def update():
        with open(Bank.database, 'w') as f:
           f.write(json.dumps(Bank.data))
           
           
           
    #create account
    def create_account(self):
        data = {
            "name": input("Enter your name:- "),
            "age":int(input("Enter your age:- ")),
            "email": input("Enter your email:- "),
            "pin":int(input("Enter your four digit pin:- ")),
            "account_number":1234,
            "balance":0
        }
        if data["age"] < 18 or len(str(data["pin"])) != 4:
            print("You are not eligible for creating an account.")
        else:
            print("Account created successfully.")
            for i in data:
                print(f"{i}: {data[i]}")
            print("Please remember your account number and pin for future transactions.")
            
            Bank.data.append(data)
            Bank.update()


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