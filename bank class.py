class Bank:
    def __init__(self, balance):
        self.balance = balance

    def show(self):
        print("Balance:", self.balance)

b = Bank(5000)
b.show()