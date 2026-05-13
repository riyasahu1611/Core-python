class Bank:

    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        print(self.__balance)

b1 = Bank()

b1.get_balance()