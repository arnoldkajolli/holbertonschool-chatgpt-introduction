#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds to complete the withdrawal")
        self.balance -= amount
        print("Withdrew ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                print("Amount must be positive")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a valid number")

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
            
            if action == 'exit':
                break
            elif action == 'deposit':
                amount = get_amount("Enter the amount to deposit: $")
                cb.deposit(amount)
            elif action == 'withdraw':
                amount = get_amount("Enter the amount to withdraw: $")
                try:
                    cb.withdraw(amount)
                except ValueError as e:
                    print(str(e))
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()