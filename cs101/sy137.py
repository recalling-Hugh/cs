import sys
import copy
n,k=map(int,sys.stdin.readline().split())
data=list(map(int,sys.stdin.readline().split()))
ans=[]
def arrangef(t,a,num,index):
    if t==k:
        ans.append(a)
        return
    for i in range(index+1,n-k+t+1):
        a_1=copy.deepcopy(a)
        a_1.append(num[i])
        arrangef(t+1,a_1,num,i)
    return
arrangef(0,[],data,-1)
ans=[list(item) for item in set(tuple(sublist) for sublist in ans)]
for i in ans:
    print(' '.join(map(str,i)))