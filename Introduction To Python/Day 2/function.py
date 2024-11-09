def mul(num1,num2):
    return (num1*num2)

def div(num1,num2):
    return (num1/num2)

def sum(num1,num2):
    return (num1+num2)

def sub(num1,num2):
    return (num1-num2)

print("Choose tow number :")
num1 = int(input())
num2 = int(input())
x = int(input("Select your choice what you want to do :"))
if(x==1):
    print(sum(num1,num2))
elif(x==2):
    print(sub(num1,num2))
elif(x==3):
    print(mul(num1,num2))
elif(x==4):
    print(div(num1,num2))
