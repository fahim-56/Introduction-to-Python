N,Q=map(int,input().split())

list = list(map(int,input().split()[:N]))

prefix=[]

prefix.append(list[0])

for i in range (1,N):
    prefix.append(list[i]+prefix[i-1])
sum=0
for i in range(0,Q):
    x,y=map(int,input().split())
    if(x==1):
        sum=prefix[y-1]
    else:
        sum=(prefix[y-1]-prefix[x-2])
    print(sum)
    sum=0