string = input()
l=0
r=0
list=[]
start=0
Total_balanced_String=0
for i,leter in enumerate(string):
    if(leter=='L'):
        l+=1
    else:
        r+=1
    if(l==r):
        list.append(string[start:i+1])
        Total_balanced_String+=1
        start=i+1
print(Total_balanced_String)
for i in list:
    print(i)