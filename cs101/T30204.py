import sys
import bisect
n,m=map(int,sys.stdin.readline().split())
core=[]
s=[]
mn=10000000
for i in range(n):
    core.append(list(map(int,sys.stdin.readline().split())))
    s.append(core[i][0]+core[i][1])
    mn=min(mn,s[i])
core.sort()
index=bisect.bisect_left(s,m)
ans=m//mn*2
for i in range(index):
    m-=core[i][0]
    ans=max(ans,i+1+m//mn*2)
print(ans)