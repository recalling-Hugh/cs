import sys
import math
data=list(map(int,sys.stdin.readline().split()))
n=data[0]
num=sorted(set(data[1:]))
if len(num)==2:
    if num[1]%num[0]==0:
        num=[num[0]]
elif len(num)==3:
    if num[1]%num[0]==0:
        if num[2]%num[0]==0:
            num=[num[0]]
        else:
            num=[num[0],num[2]]
    else:
        for i in range(num[2]//num[1]+1):
            if (num[2]-i*num[1])%num[0]==0:
                num=[num[0],num[1]]
                break
if len(num)==1:
    ans=n//num[0]
elif len(num)==2:
    ans=n//num[0]
    for i in range(ans,-1,-1):
        if (n-num[0]*i)%num[1]==0:
            ans=i+(n-num[0]*i)//num[1]
            break
else:
    p=min(math.lcm(num[0],num[1])//num[1],n//num[1])
    q=min(math.lcm(num[0],num[2])//num[2],n//num[2])
    ans=0
    for i in range(p+1):
        for j in range(q+1):
            if (n-i*num[1]-j*num[2])%num[0]==0:
                ans=max(ans,i+j+(n-i*num[1]-j*num[2])//num[0])
print(ans)