N=int(input())
Arr = list(map(int,input().split()[:N]))
mn=100000
mx=-100000
for i in Arr:
    mx=max(mx,i)
    mn=min(mn,i)

for indx,value in enumerate(Arr):
    if(value==mx):
        Arr[indx]=mn
    elif(value==mn):
        Arr[indx]=mx

for j in Arr:
    print(j,end=' ')