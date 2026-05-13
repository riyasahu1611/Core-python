class account:

    def __init__(self):
        self.__number = None
        self.__account_type = None
        self.__balance = 0.0

    # account number
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    # account type
    def get_account_type(self):
        return self.__account_type

    def set_account_type(self, account_type):
        self.__account_type = account_type

    # balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    # deposit function
    def deposit(self, amount):

        # deposit limit
        if amount > 50000:
            print("You cannot deposit more than 50000")

        else:
            self.__balance += amount

            print(amount, "deposit successful")
            print("Total Balance:", self.__balance)

a = account()

# set values
a.set_number("12345")
a.set_account_type("Saving Account")
a.set_balance(10000)

print("Account Number:", a.get_number())
print("Account Type:", a.get_account_type())
print("Balance:", a.get_balance())

# deposit calls
a.deposit(30000)
a.deposit(60000)