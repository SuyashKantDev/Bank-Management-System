import random
import datetime

class Account:
    def __init__(self, name, age, gender, mobile, account_type, initial_deposit):
        self.account_number = random.randint(100000, 999999)  # Generate random account number
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile
        self.account_type = account_type
        self.balance = initial_deposit
        self.creation_date = datetime.date.today()  # Date of account creation
        self.transaction_history = []  # To store transactions

        # Add initial deposit as a transaction
        if initial_deposit > 0:
            self.transaction_history.append({
                'type': 'Deposit',
                'amount': initial_deposit,
                'date': self.creation_date
            })

    def deposit(self, amount, date):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append({
                'type': 'Deposit',
                'amount': amount,
                'date': date
            })
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount, date):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transaction_history.append({
                    'type': 'Withdrawal',
                    'amount': amount,
                    'date': date
                })
                print(f"₹{amount} withdrawn successfully!")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount. Please try again.")

    def display_account_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Mobile Number: {self.mobile}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: ₹{self.balance}")
        print(f"Account Creation Date: {self.creation_date}")

    def display_transaction_history(self):
        print("\n--- Transaction History ---")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(f"{transaction['type']} of ₹{transaction['amount']} on {transaction['date']}")
        else:
            print("No transactions available.")


def get_date_input(prompt):
    while True:
        try:
            date_str = input(prompt + " (YYYY-MM-DD): ")
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")


def main():
    accounts = {}

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Create a new account
            name = input("Enter Account Holder Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender (Male/Female): ")
            mobile = input("Enter Mobile Number: ")
            account_type = input("Enter Account Type (Savings/Current): ")
            initial_deposit = float(input("Enter Initial Deposit Amount: ₹"))

            new_account = Account(name, age, gender, mobile, account_type, initial_deposit)
            accounts[new_account.account_number] = new_account

            print(f"Account created successfully! Your Account Number is: {new_account.account_number}")

        elif choice == "2":
            # Deposit money
            account_number = int(input("Enter Account Number: "))
            if account_number in accounts:
                amount = float(input("Enter Amount to Deposit: ₹"))
                date = get_date_input("Enter Deposit Date")
                accounts[account_number].deposit(amount, date)
            else:
                print("Account not found.")

        elif choice == "3":
            # Withdraw money
            account_number = int(input("Enter Account Number: "))
            if account_number in accounts:
                amount = float(input("Enter Amount to Withdraw: ₹"))
                date = get_date_input("Enter Withdrawal Date")
                accounts[account_number].withdraw(amount, date)
            else:
                print("Account not found.")

        elif choice == "4":
            # Display account details
            account_number = int(input("Enter Account Number: "))
            if account_number in accounts:
                accounts[account_number].display_account_details()
            else:
                print("Account not found.")

        elif choice == "5":
            # View transaction history
            account_number = int(input("Enter Account Number: "))
            if account_number in accounts:
                accounts[account_number].display_transaction_history()
            else:
                print("Account not found.")

        elif choice == "6":
            print("Thank you for using the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

