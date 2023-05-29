class Category():

    def __init__(self, ledger):
        self.my_list = []

    def deposit(self, amount, desc=False):
        if desc is False:
            desc = ""
        depo = {"amount": f'{amount}', "description": f'{desc}'}
        self.my_list.append(depo)
        print(self.my_list)
    
    def withdraw(self, amount, desc=False):
        if desc is False:
            desc = ""
        withd = {"amount": f'{-amount}', "description": f'{desc}'}
        self.my_list.append(withd)
        print(self.my_list)
    
    def get_balance():
        return True
    
    def transfer(amount, category):
        return True
    
    def check_funds(amount):
        return True 

food = Category("Food")
food.deposit(1000, "Initial Deposit")
food.withdraw(100, "Initial Withdrawal")


def create_spend_chart(categories):
    return True