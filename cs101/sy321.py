import sys
import copy
m,n=map(int,sys.stdin.readline().split())
dire=[[0,1],[1,0],[-1,0],[0,-1]]
c=[[1]*(n+2)]
for i in range(m):
    c.append([1])
    c[i+1].extend(list(map(int,sys.stdin.readline().split())))
    c[i+1].append(1)
c.append([1]*(n+2))
def walkf(x,y,t,s):
    s_1=copy.deepcopy(s)
    s_1.append((x,y))
    if x==m and y==n:
        return s_1
    ans=[0]*1000
    for i in range(4):
        if c[x+dire[i][0]][y+dire[i][1]]==0 and i+t!=3:
            tem=walkf(x+dire[i][0],y+dire[i][1],i,s_1)
            if len(tem)<len(ans):
                ans=copy.deepcopy(tem)
    return ans
l=walkf(1,1,-1,[])
for i in l:
    print(i[0],i[1])