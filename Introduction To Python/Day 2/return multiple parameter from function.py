def calculator(a,b):
    sum=a+b
    mul=a*b
    sub=a-b
    div=a/b
    return sum,mul,sub,div

result=calculator(50,10)
print(result)

# return as tuple
def calculator(a,b):
    sum=a+b
    mul=a*b
    sub=a-b
    div=a/b
    return [sum,mul,sub,div]

result=calculator(50,10)
print(result)