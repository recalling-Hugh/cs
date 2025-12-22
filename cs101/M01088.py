import sys
sys.setrecursionlimit(10000)
x=input().split()
r=int(x[0])
c=int(x[1])
come=[]
go=[[[]for i in range(c)]for j in range(r)]
x=[]
t=0
dire=[[1,0],[0,1],[-1,0],[0,-1]]
ans=[]
x.append([0]*(c+2))
for i in range(1,r+1):
    x.append([0])
    come.append([(-1,-1)]*c)
    x[i].extend(list(map(int,input().split())))
    x[i].append(0)
    ans.append([])
    for j in range(0,c):
        ans[i-1].append(0)
x.append([0]*(c+2))
for i in range(1,c+1):
    x[0][i]=x[1][i]
    x[r+1][i]=x[r][i]
for i in range(1,r+1):
    x[i][0]=x[i][1]
    x[i][c+1]=x[i][c]
def swimf(m,n,d):
    ans[m][n]+=d
    if go[m][n]==[]:
        return
    else:
        for i in go[m][n]:
            swimf(i[0],i[1],d)
        return
def slidef(m,n):
    for k in range(0,4):
        if x[m][n]<x[m+dire[k][0]][n+dire[k][1]] and ans[m+dire[k][0]-1][n+dire[k][1]-1]<ans[m-1][n-1]+1:
            print(ans)
            if come[m+dire[k][0]-1][n+dire[k][1]-1]!=(-1,-1):
                go[come[m+dire[k][0]-1][n+dire[k][1]-1][0]][come[m+dire[k][0]-1][n+dire[k][1]-1][1]].remove((m+dire[k][0]-1,n+dire[k][1]-1))
                come[m+dire[k][0]-1][n+dire[k][1]-1]=(m-1,n-1)
                go[m-1][n-1].append((m+dire[k][0]-1,n+dire[k][1]-1))
                print(m,n,go,come)
                swimf(m+dire[k][0]-1,n+dire[k][1]-1,ans[m-1][n-1]+1-ans[m+dire[k][0]-1][n+dire[k][1]-1])
            else:
                come[m+dire[k][0]-1][n+dire[k][1]-1]=(m-1,n-1)
                go[m-1][n-1].append((m+dire[k][0]-1,n+dire[k][1]-1))
                print(m,n,go,come)
                ans[m+dire[k][0]-1][n+dire[k][1]-1]=ans[m-1][n-1]+1
                slidef(m+dire[k][0],n+dire[k][1])
    return
for i in range(1,r+1):
    for j in range(1,c+1):
        flag=True
        for k in range(0,4):
            if x[i][j]>x[i+dire[k][0]][j+dire[k][1]]:
                flag=False
        if flag:
            ans[i-1][j-1]=1
            slidef(i,j)
for i in range(0,r):
    for j in range(0,c):
        t=max(t,ans[i][j])
print(t)