class Bank:
    bankbalance = 0

    def account(self):
        self.account_name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.amount = int(input("Enter amount: "))
        Bank.bankbalance = Bank.bankbalance + self.amount

    @classmethod
    def showbankbal(cls):
        print("Total Balance: ", cls.bankbalance)


LC = dict()

while True:
    newAccount = Bank()
    key = newAccount.account()
    LC.setdefault(key, newAccount)
    ch = input("Add More y/n? ")
    if ch == "n": break

Bank.showbankbal()
