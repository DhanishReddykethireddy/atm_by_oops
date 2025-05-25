
class atm_functions():
    def __init__(self,bank,location,balance):
        self.bank=bank
        self.location=location
        self.balance=balance
    def options(self):
        print('atm options')
        print("1.credit")
        print('2.debit')
        print('3.balance enquary')
        print('4.exit')
    def choices(self):
        choice=input('choose your choice from the atm options:')
        if choice in ['1','2','3','4']:
            return choice
        else:
            print('choose the correct option from the atm options')
    def credit(self):
        credit_amount=float(input('enter the creidt amount:'))
        if credit_amount <=0:
            print('enter the correct amount')
        else:
            self.balance+=credit_amount
            print(f'Rs{credit_amount} is added to your account successfully')
    def debit(self):
        debit_amount=float(input('enter the amount to be debited:'))
        if debit_amount<=0:
            print('enter the correct amount')
        else:
            if debit_amount > self.balance:
                print('insufficient balance in your bank')
            else:
                self.balance-=debit_amount
                print(f'Rs{debit_amount} has debited from your account')   
    def enquary(self):
        print(f'the balance in your bank acount is {self.balance}') 
       
atm=atm_functions('State Bank of India','hyderabad',500)
print('-'*50)
print(f"wecome to {atm.bank} atm,{atm.location}")
print(' '*5,'Welcome to the SBI atm services')
print('-'*50)
atm.options()
while True:
    option=atm.choices()
    if option == '1':
        atm.credit()
    elif option == '2':
        atm.debit()
    elif option == '3':
        atm.enquary()
    elif option == '4':
        print('-'*50)
        print('Thank you for visiting SBI atm services')
        print('Have a nice day')
        print('-'*50)
        break
        