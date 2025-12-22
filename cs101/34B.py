import sys
data=list(map(int,sys.stdin.readline().split()))
n=data[0]
m=data[1]
data=list(map(int,sys.stdin.readline().split()))
data.sort()
ans=0
for i in range(m):
    if data[i]>0:
        break
    ans-=data[i]
print(ans)