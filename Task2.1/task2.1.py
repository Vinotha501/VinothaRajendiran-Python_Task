# Design a Bank Account System

class BankAccount:
    def __init__(self, Account_number, Account_holder_name, Balance, Account_type):
       self.Account_number = Account_number
       self.Account_holder_name = Account_holder_name
       self.Balance = Balance
       self.Account_type = Account_type
       self.deposit_history = []
       self.withdraw_history = []
       

    # deposit
    def deposit(self, amount):
        self.Balance+= amount
        self.deposit_history.append(amount)
        print(f"Amount deposited in your account is Rs.{amount}")
        

    # withdraw
    def withdraw(self, amount):
        if self.Balance >=amount:
           self.Balance-= amount
           self.withdraw_history.append(amount)
           print (f"Amount Withdrawed in your account is Rs.{amount}")
        else:
            print ("Insufficient balance")
        
    # enquiry
    def enquiry(self):
        print ("Available balance : ", self.Balance)


# Savings Account
class SavingsAccount (BankAccount):
    def  __init__(self, Account_number, Account_holder_name, Balance,  Interest_rate):
        super().__init__(Account_number, Account_holder_name, Balance, Interest_rate)
        self.Interest_rate = Interest_rate

    def Interest_calculate(self,):
        Interest = self.Balance * self.Interest_rate
        self.Balance += Interest
        print (f"Interest added is Rs.{Interest} and the new balance is Rs.{self.Balance}")

# Current account
class CurrentAccount(BankAccount):
    def __init__ (self,Account_number, Account_holder_name, Balance,Overdraft_amount):
        super().__init__(Account_number, Account_holder_name, Balance,Overdraft_amount)
        self.Overdraft_amount = Overdraft_amount

    def Overdraft_protection (self,amount):
         if self.Balance + self.Overdraft_amount >= amount: 
             self.Balance -= amount
             print (f"Overdraft protection amount is Rs.{amount} and Current balance is Rs.{self.Balance}") 

         else:
             print ("Insufficient balance and Overdraft protection")

    def transaction_history(self):
        print("Transcation  History:")
        print("Amount deposited: ", self.deposit_history)
        print("Amount withdrawed: ", self.withdraw_history)

print("Savings Account:")
S = SavingsAccount (8729173546, "Hari", 1000.0, 0.05)
S.deposit(500)
S.withdraw(200)
S.enquiry()
S.Interest_calculate()


print("\n")

print("Current Account:")
C= CurrentAccount (8729173546, "Hari", 1000.0, 0.05)
C.deposit(400)
C.withdraw(200)
C.enquiry()
C.Overdraft_protection(200)
C.transaction_history()





    