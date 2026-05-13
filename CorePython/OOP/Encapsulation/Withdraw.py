class account:

    def __init__(self):
        self.__number = None
        self.__account_type = None
        self.__balance = 0.0
        self.__withdraw_count = 0

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

    # withdraw function
    def withdraw(self, amount):

        # only 5 withdrawals allowed
        if self.__withdraw_count >= 5:
            print("Withdrawal limit exceeded")

        # cannot withdraw more than 5000
        elif amount > 5000:
            print("You cannot withdraw more than 5000")

        # insufficient balance
        elif amount > self.__balance:
            print("Insufficient balance")

        # successful withdrawal
        else:
            self.__balance -= amount
            self.__withdraw_count += 1

            print(amount, "withdraw successful")
            print("Remaining Balance:", self.__balance)
            print("Withdrawal Count:", self.__withdraw_count)


# object create
a = account()

# set values
a.set_number('12345')
a.set_account_type("Saving Account")
a.set_balance(10000)

# print details
print("Account Number:", a.get_number())
print("Account Type:", a.get_account_type())
print("Balance:", a.get_balance())

# withdraw calls
a.withdraw(1000)
a.withdraw(2000)
a.withdraw(3000)
a.withdraw(6000)  # more than 5000
a.withdraw(500)
a.withdraw(200)
a.withdraw(100)  # 6th withdrawal
