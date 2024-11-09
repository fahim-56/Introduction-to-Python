input=input()

list=[]
for x in input:
    list.append(x)
list1 = list.copy()
list.reverse()

flag = False
for l in list:
    if(l=='0' and flag == False):
        continue
    elif(l!='0'):
        flag=True
        print(l,end="")
    elif(l=='0' and flag == True):
        print(l,end="")

print()
if(list1==list):
    print("YES")
else:
    print("NO")

# inp = input()
# k = str(int(inp[::-1]))
# print(k)
# if inp == inp[::-1]:
#     print("YES")
# else:
#     print("NO")
