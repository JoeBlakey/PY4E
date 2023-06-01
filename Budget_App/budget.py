class Category():
    
    def __init__(self, name):
        self.ledger = []
        self.current_balance = 0
        self.pos_funds = True
        self.name = name

    def __repr__(self):
        output = ""
        title = f'{self.name}'
        title_line = title.center(30, '*')
        for n in self.ledger:
            for k,v in n.items():
                output = output + v + "\n"
        cat_output = title_line + "\n" + output
        return cat_output

    def deposit(self, amount, desc=False):
        if desc is False:
            desc = ""
        depo = {"amount": f'{amount}', "description": f'{desc}'}
        self.ledger.append(depo)
        self.current_balance = self.current_balance + amount
        print(self.ledger)
    
    def withdraw(self, amount, desc=False):
        if desc is False:
            desc = ""
        withd = {"amount": f'{-amount}', "description": f'{desc}'}
        self.check_funds(amount)
        if self.pos_funds:
            self.current_balance = self.current_balance - amount
            self.ledger.append(withd)
            print(self.ledger)
            return True
        else:
            return False
    
    def get_balance(self):
        return self.current_balance
    
    def transfer(self, amount, new_cat):
        # Needs destination adding
        if (self.withdraw(amount, f"Transfer to ")):
            print("Transfer Successful")
            new_cat.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            print("Transfer Failed")
            return False        
    
    def check_funds(self, amount):
        if amount > self.current_balance:
            print("No")
            self.pos_funds = False
            return False
        else:
            print("Yes")
            self.pos_funds = True
            return True 

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
print(clothing.get_balance())
print(food)

def create_spend_chart(categories):
    return True