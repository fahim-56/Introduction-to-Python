from collections import Counter
N=int(input())
list=list(map(int,input().split()[:N]))

freq=Counter(list)

remove=0
for i in list:
    if(i>freq[i]):
        remove+=freq[i]
        freq[i]=i

    elif(i<freq[i]):
        remove+=(freq[i]-i)
        freq[i]=i

print(remove)