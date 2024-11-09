balance = 50000

def shoping(item,price):
    # by using global keyword we can change global value
    global balance 
    balance -=price

shoping("Book",1000)
print(balance)