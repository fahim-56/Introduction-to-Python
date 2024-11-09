num = int(input())
list = list(map(int, input().split()[:num]))

mx=-99999
mx_indx = 0
mn=99999
mn_indx = 0
for indx,value in enumerate(list):
    if(mx<value):
        mx=value
        mx_indx=indx
    if(mn>value):
        mn=value
        mn_indx=indx

new=[]
for indx,value in enumerate(list):
    if(value == mx):
        new.append(mn)
    elif(value == mn):
        new.append(mx)
    else:
        new.append(value)


for i in new:
    print(i,end=" ")