duble = lambda a : a*2
print(duble(28))

sqr = lambda a : a**2
print(sqr(2))

add =lambda a,b: a+b
print(add(2,5))

div =lambda a,b :a/b
print(div(5,2))

mylist = [10,20,30,40,50,60,70]
print(mylist)
print(list(map(duble,mylist)))

print(list(map(lambda x: x-10,mylist)))