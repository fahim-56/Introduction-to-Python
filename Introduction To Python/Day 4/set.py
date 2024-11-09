numbers=[10,20,40,30,50,20,10]
print(numbers)
set1=set(numbers)
print(set1)

myset={10,20,40,30,50,20,10}
print(myset)

myset.remove(20)
print(myset)

myset.add(100)
print(myset)

for x in myset:
    print(x)

if 50 in myset:
    print(50 ,"Exist")

A={10,20,30}
B={10,15,20,25}
print(A & B)
print(A | B)