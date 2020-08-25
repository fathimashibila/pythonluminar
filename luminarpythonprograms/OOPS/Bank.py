import datetime
class person:
    def setvalues(self,pname,age):
        self.age=age
        self.pname=pname
    def printvalues(self):
        print(self.pname)
        print(self.age)
class bank(person):
    def __init__(self,acntno,personalname,balance,bankname):
        self.acntno=acntno
        self.personalname=personalname
        self.balance=3000
        self.bankname="SBI"
        print("Account number:",acntno)
        print("Name:",personalname)
        print("Account balance:",balance)
        print("Bank name:",bankname)
    def witdraw(self,wit):
        self.balance-=wit
        if(self.balance>=0):
            print("balance after witdraw:",self.balance)
        else:
            print("you have no insufficent amount")
            self.balance+=wit

    def deposit(self,depo):
        self.balance+=depo
        print("Balance After deposit:",self.balance,"on",datetime.date.today())
    def balanceEnquiry(self):
        print("Current balance:",self.balance)

obj1=bank(1021,"Rahul",25000,"sbi")
obj1.balanceEnquiry()
obj1.deposit(40000)
obj1.setvalues("rahul",44)
obj1.printvalues()