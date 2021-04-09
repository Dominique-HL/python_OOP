class User:

    def __init__(self, username):
        self.name = username			
        self.account_balance = 0		
    
    def make_deposit(self, amount):	
        
        self.account_balance += amount
        print(f"{self.name} depositaste ${amount} a tu cuenta bancaria")
        return self

    def make_withdrawal(self, amount):   
        
        self.account_balance -= amount 
        print(f"{self.name} retiraste ${amount} desde tu cuenta bancaria")
        self.display_user_balance()
        return self
        
    def display_user_balance(self):
        print(f"Usuario: {self.name},","Saldo: $" + str(self.account_balance))
        return self

benito = User("Benito Dachs")

benito.make_deposit(200).make_withdrawal(30).make_deposit(20).make_withdrawal(100).display_user_balance()