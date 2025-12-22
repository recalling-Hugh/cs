n=int(input())
ans=0
for i in range(0,n):
    data=list(map(int,input().split()))
    s=data[0]+data[1]+data[2]
    if s>=2:
        ans+=1
print(ans)