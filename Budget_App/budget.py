class Category():

    def __init__(self, ledger):
        self.my_list = []
        self.current_balance = 0
        self.pos_funds = True

    def deposit(self, amount, desc=False):
        if desc is False:
            desc = ""
        depo = {"amount": f'{amount}', "description": f'{desc}'}
        self.my_list.append(depo)
        self.current_balance = self.current_balance + amount
        print(self.my_list)
    
    def withdraw(self, amount, desc=False):
        if desc is False:
            desc = ""
        withd = {"amount": f'{-amount}', "description": f'{desc}'}
        self.check_funds(amount)
        if self.pos_funds:
            self.current_balance = self.current_balance - amount
            self.my_list.append(withd)
            print(self.my_list)
            return True
        else:
            return False
    
    def get_balance(self):
        return self.current_balance
    
    def transfer(amount, category):
        return True
    
    def check_funds(self, amount):
        if amount > self.current_balance:
            print("No")
            self.funds = False
            return False
        else:
            print("Yes")
            self.funds = True
            return True 

food = Category("Food")
food.deposit(1000, "Initial Deposit")
food.deposit(1000, "Initial Deposit")
food.withdraw(300, "Initial Withdrawal")


def create_spend_chart(categories):
    return True