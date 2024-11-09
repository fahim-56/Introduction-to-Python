double = lambda x : x*2

mylist = [10,20,30,40,50,60,70]
print(mylist)

print(list(map(double,mylist)))
minus_10 = map(lambda x: x-10,mylist)
print(list(minus_10))