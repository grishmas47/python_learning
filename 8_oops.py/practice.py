class Account:
    def __init__(self, balance, accno):
        self.balance=balance
        self.accno=accno

    def debit(self, deb_amt):
        self.balance=self.balance-deb_amt
        print("Rs.", self.balance, "was debited")

    def credit(self, cred_amt):
        self.balance=self.balance+cred_amt
        print("Rs.", self.balance, "was credited")

    def print_balance(self):
        print("Your updated balance is Rs:", self.balance)

acc1=Account(10000, 1111111111)
acc1.debit(1000)
acc1.credit(2000)
acc1.print_balance()

acc2=Account(50000, 2222222)
acc2.debit(3000)
acc2.credit(12000)
acc2.print_balance()