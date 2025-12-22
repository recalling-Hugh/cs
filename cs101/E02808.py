data=list(map(int,input().split()))
n=data[0]
m=data[1]
ans=0
flag=[True]*(n+1)
for i in range(m):
    data=list(map(int,input().split()))
    flag=flag[:data[0]]+[False]*(data[1]-data[0]+1)+flag[data[1]+1:]
for b in flag:
    if b:
        ans+=1
print(ans)