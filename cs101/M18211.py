import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
data.sort()
a=0
ans=0
while data!=[]:
    if n>=data[0]:
        n-=data[0]
        a+=1
        data.remove(data[0])
    elif a>0:
        n+=data[-1]
        a-=1
        data.remove(data[-1])
    else:
        break
    ans=max(ans,a)
print(ans)