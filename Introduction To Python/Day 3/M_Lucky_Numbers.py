x,y = map(int, input().split())
y += 1
ase = False
for k in range(x,y):
    m = str(k)
    flag = True
    for i in m:
        if(i != '4' and i != '7'):
            flag =False
            break
    if(flag == True):
        print(k,end=" ")
        ase =True
if(ase == False):
    print(-1)  