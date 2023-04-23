class Bank:
    bank_balance = 0

    def __init__(self):
        self.account_name = None
        self.age = None
        self.amount = None

    def account(self):
        self.account_name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.amount = int(input("Enter amount: "))
        if self.amount:
            Bank.bank_balance += self.amount
            return self.account_name

    @classmethod
    def show_bank_balance(cls):
        print("Total Balance: ", cls.bank_balance)


LC = dict()

n = int(input("Enter number of accounts: "))
for i in range(n):
    new_account = Bank()
    key = new_account.account()
    if key:
        LC.setdefault(key, new_account)

Bank.show_bank_balance()
