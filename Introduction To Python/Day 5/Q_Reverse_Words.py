string=input()
str=string.split()
list=[]
for s in str:
    list.append(s[::-1])

print(" ".join(list))
