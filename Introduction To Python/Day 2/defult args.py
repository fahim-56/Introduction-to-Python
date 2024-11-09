#a,b must c,d,e if want
def sum(a,b,c=0,d=0,e=0):
    return(a+b+c+d+e)

print(sum(5,6))
print(sum(5,6,7))
print(sum(5,6,7,8))
print(sum(5,6,7,8,9))

def do_sum(*args):
    return args
print(do_sum(3,4))

def do_sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
result=do_sum(4,5,6)
print(result)