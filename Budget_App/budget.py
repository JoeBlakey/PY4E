class Category:
  
  def __init__(self, categories):
    self.categories = categories
    self.ledger = []
    self.spent = 0
    self.percentage_spent = 0

  def __str__(self):
    categories_length = len(self.categories)
    output = ""
    
    #First Line
    for x in range(0, int((30-categories_length)/2)):
      output += "*"
    if (categories_length % 2) != 0:
      output += "*"
    output += self.categories
    for x in range(0, int((30-categories_length)/2)):
      output += "*"
    output += "\n"

    #Description + Amount
    line = []
    for x in self.ledger:
      line = x['description'][0:23]
      for y in range(len(line), 23):
        line += " "

      amt = str("{:.2f}".format(x['amount']))   
      for y in range(0, 7 % len(amt)):
        line += " "
      line += amt + "\n"
      output += line
  
    #Category Total Balance
    output += "Total: " + str(self.get_balance())
    
    return output

  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.spent += -amount
      return True
    else:
      return False
  
  def get_balance(self):
    balance = 0
    for x in self.ledger:
      balance += x['amount'] 
    return balance

  def transfer(self, amount, new_cat):
    if self.withdraw(amount, "Transfer to " + new_cat.categories):
      new_cat.deposit(amount, "Transfer from " + self.categories)
      return True
    else:
      return False
  
  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False
  
def create_spend_chart(categories):
  
  total_spent = 0
  for category in categories:
    total_spent += category.spent

  for category in categories:
    category.percentage_spent = int(category.spent*100/total_spent) 

  output = "Percentage spent by category\n"
  for x in range (100, -1, -10):
    output += str(x).rjust(3) + "| "
    for y in categories:
      if y.percentage_spent >= x:
        output += "o  "
      else:
        output += "   "
    output += "\n"

  output += "    -"
  for x in range(0, len(categories)):
    output += "---"
  output += "\n"

  #List Comprehension - max len of categories name
  max_len_categories_name = max([len(category.categories) for category in categories])
  
  for x in range(0, max_len_categories_name):
    output += "     "
    for category in categories:
      if x < len(category.categories):
        output += category.categories[x] + "  "
      else:
        output += "   "
    if x != max_len_categories_name - 1:
      output += "\n"

  return output