class Category():
    
    def __init__(self, name):
        self.ledger = []
        self.current_balance = 0
        self.deposited = 0
        self.spent = 0
        self.pos_funds = True
        self.name = name

    def __repr__(self):
        ledger = ""
        total = 0
        title = f'{self.name}'
        title_line = title.center(30, '*')
        for n in self.ledger:
            line_desc = "{:<23}".format(n["description"])
            line_amount = "{:>7.2f}".format(float(n["amount"]))
            ledger = ledger + f"{line_desc[:23]}{line_amount:<7}" + "\n"
            total = total + float(n["amount"])
        total = str(total)
        cat_output = title_line + "\n" + ledger + "Total: " + total
        return cat_output

    def deposit(self, amount, desc=False):
        if desc is False:
            desc = ""
        depo = {"amount": f'{amount}', "description": f'{desc}'}
        self.ledger.append(depo)
        self.current_balance = self.current_balance + amount
        self.deposited = self.deposited + amount
        print(self.ledger)
    
    def withdraw(self, amount, desc=False):
        if desc is False:
            desc = ""
        withd = {"amount": f'{-amount}', "description": f'{desc}'}
        self.check_funds(amount)
        if self.pos_funds:
            self.current_balance = self.current_balance - amount
            self.spent = self.spent + amount
            self.ledger.append(withd)
            print(self.ledger)
            return True
        else:
            return False
    
    def get_balance(self):
        return self.current_balance
    
    def transfer(self, amount, new_cat):
        # Needs destination adding
        if (self.withdraw(amount, f"Transfer to {new_cat.name}")):
            print("Transfer Successful")
            new_cat.deposit(amount, f"Transfer from {self.name}")
            self.spent = self.spent + amount
            self.deposited = self.deposited + amount
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

def create_spend_chart(self):
    n = 0
    num_args = len(self)
    while n < num_args:
        percentage = (self[n].spent / self[n].deposited) * 100
        rounded_perc = round(percentage/10)*10
        n = n + 1
    title = "Percentage Spent by Category\n"

    chart = ""
    for value in reversed(range(0,101,10)):
        chart += str(value).rjust(3)+"|"
        if rounded_perc >= value:
            chart += " o "
        else:
            chart += "   "
        chart += "\n"

    print(chart)

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
print(clothing.get_balance())
print(food)
print(clothing)
create_spend_chart([food, clothing])