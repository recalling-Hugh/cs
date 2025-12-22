import sys
from functools import lru_cache
@lru_cache(maxsize=None)
def findf(a,target):
    results=[]
    def dfs(start,path,c):
        if target==c:
            results.append(path[:])
            return
        for i in range(start,len(a)):
            if a[i]==a[i-1] and i>start:
                continue
            if c+a[i]>target:
                break
            path.append(a[i])
            dfs(i+1,path,c+a[i])
            path.pop()
        return
    dfs(0,[],0)
    return results
def combinef(content,target):
    for c in content:
        ctemp=content[:]
        ctemp.remove(c)
        temp=target[:]
        flag=False
        for i in c:
            try:
                temp.remove(i)
            except ValueError:
                flag=True
                break
        if flag:
            continue
        if not temp:
            return True
        if combinef(ctemp,temp):
            return True
    return False
data=sys.stdin.read().splitlines()
for i in range(0,len(data),2):
    if i+1>=len(data):
        break
    n=int(data[i])
    if n==0:
        break
    num=list(map(int,data[i+1].split()))
    num.sort()
    mx=0
    s=0
    for j in num:
        s=s+j
        mx=max(mx,j)
    for j in range(mx,s+1):
        if s%j!=0:
            continue
        r=findf(num,j)
        if combinef(r,num):
            print(j)
            break