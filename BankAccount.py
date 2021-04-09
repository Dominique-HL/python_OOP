class BankAccount:

	
    def __init__(self, username,  int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        self.name = username

    def deposit(self, amount):

        self.balance += amount
        return self

	
    def withdraw(self, amount):

        if amount > self.balance:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
        self.balance -= amount
        return self
		
        
	
    def display_account_info(self):

		
        
        print(f"Usuario : {self.name}","Saldo : $" + str(self.balance))
        return self
       

	
    def yield_interest(self):

        self.balance += self.balance * self.int_rate / 100
        return self

class User:

    def __init__(self, username, int_rate, balance):
        self.name = username			
        self.account = BankAccount(username, int_rate,balance)

monty = User("Monty Python",1,500)
benito = User("Benito Dachs",2,1000)

#En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la información de la 
# cuenta en una sola línea de código es decir, encadenamiento)
monty.account.deposit(100).deposit(200).deposit(300).withdraw(300).display_account_info()
print ()
#En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la información de la 
#cuenta en una sola línea de código (es decir, encadenamiento)
benito.account.deposit(50).deposit(200).withdraw(10).withdraw(500).withdraw(400).withdraw(500).display_account_info()