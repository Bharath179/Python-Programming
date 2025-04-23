'''class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

# Creating an object of BankAccount
account = BankAccount("John")

# Accessing methods to deposit and withdraw
account.deposit(1000)
account.withdraw(500)

# Accessing the private balance attribute via a method
print(account.get_balance())  # Output: 500'''




class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def get_balance(self):  # Getter method
        return self.__balance

    def deposit(self, amount):  # Deposit method
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Amount to deposit should be greater than 0.")

    def withdraw(self, amount):  # Withdraw method
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

# Create an object of the BankAccount class
account = BankAccount("John Doe", 5000)

account.deposit(1000)   # Output: Deposited 1000. New balance: 6000
account.withdraw(2000)  # Output: Withdrew 2000. New balance: 4000
print(account.get_balance())  # Output: 4000
