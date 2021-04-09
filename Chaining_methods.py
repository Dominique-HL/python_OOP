class User:

    def __init__(self, username):
        self.name = username			
        self.account_balance = 0		

    def make_deposit(self, amount):	
        
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):   
        
        self.account_balance -= amount 
        return self
        
    def display_user_balance(self):
        print(f"Usuario: {self.name},","Saldo: $" + str(self.account_balance))
        
        
guido = User("Guido van Rossum")
monty = User("Monty Python")
benito = User("Benito Dachs")

guido.make_deposit(100).make_deposit(200).make_deposit(100).make_withdrawal(50).display_user_balance()
monty.make_deposit(50).make_deposit(200).make_withdrawal(50).make_withdrawal(50).display_user_balance()
benito.make_deposit(200).make_withdrawal(30).make_deposit(20).make_withdrawal(100).display_user_balance()



