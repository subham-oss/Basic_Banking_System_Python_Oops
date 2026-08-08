import json
import random
import string
from pathlib import Path


class Bank:
    DATABASE = Path("data.json")

    def __init__(self):
        self.data = self._load_data()

    # -----------------------------
    # Load database
    # -----------------------------
    def _load_data(self):
        try:
            if self.DATABASE.exists():
                with open(self.DATABASE, "r") as file:
                    return json.load(file)

            print("Database file not found. Starting with empty database.")
            return []

        except json.JSONDecodeError:
            print("Invalid JSON database. Starting with empty database.")
            return []

        except Exception as error:
            print(f"Error loading database: {error}")
            return []

    # -----------------------------
    # Update database
    # -----------------------------
    def _update(self):
        try:
            with open(self.DATABASE, "w") as file:
                json.dump(self.data, file, indent=4)

        except Exception as error:
            raise Exception(f"Database update failed: {error}")

    # -----------------------------
    # Generate account number
    # -----------------------------
    def _generate_account_number(self):
        while True:
            letters = "".join(
                random.choices(string.ascii_uppercase, k=3)
            )

            numbers = "".join(
                random.choices(string.digits, k=3)
            )

            special = random.choice("!@#$%^&*")

            account_number = letters + numbers + special

            if not any(
                account["account_number"] == account_number
                for account in self.data
            ):
                return account_number

    # -----------------------------
    # Find account
    # -----------------------------
    def _find_account(self, account_number, pin):
        for account in self.data:
            if (
                account["account_number"] == account_number
                and account["pin"] == pin
            ):
                return account

        return None

    # -----------------------------
    # Create account
    # -----------------------------
    def create_account(self, name, age, email, pin):
        if not name.strip():
            return False, "Name cannot be empty."

        if age < 18:
            return False, "You must be at least 18 years old."

        if not 1000 <= pin <= 9999:
            return False, "PIN must be exactly 4 digits."

        if "@" not in email or "." not in email:
            return False, "Please enter a valid email."

        account = {
            "name": name.strip(),
            "age": age,
            "email": email.strip(),
            "pin": pin,
            "account_number": self._generate_account_number(),
            "balance": 0
        }

        self.data.append(account)
        self._update()

        return True, account

    # -----------------------------
    # Deposit
    # -----------------------------
    def deposit(self, account_number, pin, amount):
        account = self._find_account(account_number, pin)

        if account is None:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 100000:
            return False, "Maximum deposit is ₹1,00,000."

        account["balance"] += amount
        self._update()

        return True, f"₹{amount:,.2f} deposited successfully."

    # -----------------------------
    # Withdraw
    # -----------------------------
    def withdraw(self, account_number, pin, amount):
        account = self._find_account(account_number, pin)

        if account is None:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > account["balance"]:
            return False, "Insufficient balance."

        account["balance"] -= amount
        self._update()

        return True, f"₹{amount:,.2f} withdrawn successfully."

    # -----------------------------
    # Account details
    # -----------------------------
    def get_details(self, account_number, pin):
        account = self._find_account(account_number, pin)

        if account is None:
            return None

        return {
            "account_number": account["account_number"],
            "name": account["name"],
            "age": account["age"],
            "email": account["email"],
            "balance": account["balance"]
        }

    # -----------------------------
    # Update details
    # -----------------------------
    def update_details(
        self,
        account_number,
        pin,
        name=None,
        email=None,
        new_pin=None
    ):
        account = self._find_account(account_number, pin)

        if account is None:
            return False, "Invalid account number or PIN."

        if name is not None:
            if not name.strip():
                return False, "Name cannot be empty."

            account["name"] = name.strip()

        if email is not None:
            if "@" not in email or "." not in email:
                return False, "Invalid email."

            account["email"] = email.strip()

        if new_pin is not None:
            if not 1000 <= new_pin <= 9999:
                return False, "PIN must be exactly 4 digits."

            account["pin"] = new_pin

        self._update()

        return True, "Account details updated successfully."

    # -----------------------------
    # Delete account
    # -----------------------------
    def delete_account(self, account_number, pin):
        account = self._find_account(account_number, pin)

        if account is None:
            return False, "Invalid account number or PIN."

        self.data.remove(account)
        self._update()

        return True, "Account deleted successfully."