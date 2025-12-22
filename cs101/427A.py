n=int(input())
data=list(map(int,input().split()))
s=0
ans=0
for i in data:
    if s+i<0:
        ans+=1
    else:
        s+=i
print(ans)