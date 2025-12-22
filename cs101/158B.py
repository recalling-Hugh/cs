import math
n=int(input())
data=list(map(int,input().split()))
bucket=[0,0,0,0,0]
ans=0
for i in data:
    bucket[i]+=1
ans+=bucket[4]+bucket[3]
bucket[1]-=bucket[3]
ans+=math.ceil(bucket[2]/2)
if bucket[2]%2==1:
    bucket[1]-=2
ans+=max(0,math.ceil(bucket[1]/4))
print(ans)