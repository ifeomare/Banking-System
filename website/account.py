class Account:
    def __init__(self, accnum, bal, un, pw, pin, fn, mn, ln):
        self.id = accnum
        self.username = un
        self.password = pw
        self.fname = fn
        self.mname = mn
        self.lname = ln
        self.balance = bal
    def getid(self):
        return self.id
    def getf(self):
        return self.fname
    def checkBalance(self):
        return self.balance
    def deposit(self, dep):
        self.balance += dep
    def withdraw(self, wd):
        if wd <= self.balance:
            self.balance -= wd
            return True
        return False