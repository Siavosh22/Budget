class Category:
    def __init__(self, name): 
        self.name = name
        self.ledger =[]
        self.funds=0
      
    def check_funds(self,amount):
      if self.amount < amount:
        return False
      else:
        return True
      
    def deposit(self , amount ,description =""):
      self.ledger.append ({"amount":amount,"description":description})
      self.funds += amount
      
    def withdraw(self, amount, description=""):
      if self.check_funds(amount) == True:
        self.amount -=amount
        self.ledger.append({"amount":-amount,"description":description})
        return True
      else:
        return False

    def get_balance(self):
      return self.amount

    def transfer(self,amount,category):
      if self.check_funds(amount)==True:
        self.amount-=amount
        self.ledger.append({"amount": -amount,"description":"Transfer to"+category.category})
        category.ledger.append({"amount": amount,"description":"Transfer from "+self.category})
        return True
      else:
        return False

    def __str__(self):
      result=""
      result+=self.name.center(30 , "*")+"\n"
      for transaction in self.ledger:
        if len (transaction["description"]) > 23:
          result+= transaction["description"][0:23]
        else:
          result+= transaction["description"][0:23].ljust(23)
        result+="{0:.2f}".format(transaction["amount"]).rjust(7)
        result+="\n"
      result+="Total : {}".format(self.funds)
      return result
        
def create_spend_chart(categories):
  s = "Percentage spent by category\n"
  sum = 0
  withdraws = {}
  for x in categoties :
    withdraws[x.name] = 0
    for y in x.ledger:
      if y["amount"]< 0:
        withdraws[x.name] += y["amount"]
    withdraws[x.name] = withdraws[x.name]
  for x in withdraws:
    sum += withdraws[x]
  for x in withdraws:
    withdraws[x] = int (withdraws[x]/sum * 100)

  for i in range (100 , -1 , -10):
    s+= str(i).rjust(3)+"| "
    for x in categories :
      if withdraws[x.name]>= i :
        s+= "o  "
      else:
        s+= "    "

    s+="\n"
  s+=" "*4+"-"*(1+len(categories)*3)+"\n"

  maxlen = 0
  for x in categories:
    if len(x.name)> maxlen:
      maxlen = len(x.name)
    for i in range(maxlen):
      s += "  "*5
      for x in categories:
        if len (x.name)> i :
          s +=x.name[i]+"  "
        else:
          s+="  "*3
      s+="\n"
    return s[0:-1]
if __name__ == "__main__":
  food = categoy("food")
  entertainment = categoy("entertainment")
  business = categoy("business")
  food.deposit   (900,"deposite")
  entertainment.deposit (900,"deposite")
  business.deposit (900,"deposite")
  food.withdraw (105.55)
  entertainment.withdraw (33.40)
  business.withdraw (10.99)
  actual = create_spend_chart ([food,entertainment,business])
  print(actual)
  
  
  
  
