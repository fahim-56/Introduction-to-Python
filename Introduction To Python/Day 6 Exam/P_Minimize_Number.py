N=int(input())
list=list(map(int,input().split()[:N]))

count=0
while True:
    flag=True
    for i in list:
        if(i%2!=0):
            flag=False

    if(flag==False):
        break
    
    list= [x//2 for x in list]
    count+=1

print(count)