class User:
    def __init__(self, username,):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro

# agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
    	self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

#agrega el métodp make_withdrawal
    def make_withdrawal(self,amount):   #toma un argumento que es el monto del retiro
        self.account_balance -= amount  # la cuenta del usuario específico disminuye por la cantidad del valor retirado

#agrega el método display_user_balance
    def display_user_balance(self):
        print(f"Usuario: {self.name},","Saldo: $" + str(self.account_balance))
        

guido = User("Guido van Rossum")
monty = User("Monty Python")
benito = User("Benito Dachs")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(100)
guido.make_withdrawal(50)
""" print(guido.name)	
print(guido.account_balance) """
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
""" print(monty.name)	
print(monty.account_balance) """
monty.display_user_balance()


benito.make_deposit (200)
benito.make_withdrawal(30)
benito.make_withdrawal(20)
benito.make_withdrawal(100)
""" print(benito.name)
print(benito.account_balance)	 """
benito.display_user_balance() 

