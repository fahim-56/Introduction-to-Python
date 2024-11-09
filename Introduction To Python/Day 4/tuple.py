mytuple='Fahim','Kawshik','Tonmoy','Arbs',56
print(mytuple)

# mytuple[0]='Nai' not allow to change tuple

for i in mytuple:
    print(i)

print(len(mytuple))

print(type(mytuple))

another=[1,2,3],[4,5,6]
print(type(another))
print(another[0])

another[0][1]=10 # but changing list's values in tuple are alowed
print(another)
