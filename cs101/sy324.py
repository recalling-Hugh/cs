import sys
import copy
m,n=map(int,sys.stdin.readline().split())
dire=[[0,1],[1,0],[-1,0],[0,-1]]
c=[[1]*(n+2)]
ans=[]
for i in range(m):
    c.append([1])
    c[i+1].extend(list(map(int,sys.stdin.readline().split())))
    c[i+1].append(1)
    ans.append([-1]*n)
c.append([1]*(n+2))
ans[0][0]=0
layer=[(0,0)]
for i in range(m*n):
    temp=[]
    for j in layer:
        num=ans[j[0]][j[1]]+1
        for k in dire:
            if c[j[0]+k[0]+1][j[1]+k[1]+1]==0 and ans[j[0]+k[0]][j[1]+k[1]]==-1:
                temp.append((j[0]+k[0],j[1]+k[1]))
                ans[j[0]+k[0]][j[1]+k[1]]=num
    layer=copy.deepcopy(temp)
for i in ans:
    print(' '.join(map(str,i)))