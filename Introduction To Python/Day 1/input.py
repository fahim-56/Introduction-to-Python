number1 = input("Choose your number : ")
print("Your choosen number is", number1)
# by defult user input is string
print(type(number1))

number2 = input("Choose your number : ")
print("Your choosen number is", number2)
# by defult user input is string
print(type(number2))

print("Before Typecasting : ",number1+number2)

number1 =int(number1)
print(type(number1))

number2 =int(number2)
print(type(number2))

print("After Typecasting : ",number1+number2)
