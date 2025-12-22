import sys
data=list(map(int,sys.stdin.readline().split()))
n=data[0]
m=data[1]
data=[[0]*(m+2)]
ans=[]
x=[1,1,1,0,0,-1,-1,-1]
y=[1,0,-1,1,-1,1,0,-1]
for i in range(n):
    data.append([0])
    data[i+1].extend(list(map(int,sys.stdin.readline().split())))
    data[i+1].extend([0])
    ans.append([0]*m)
data.append([0]*(m+2))
for i in range(n):
    for j in range(m):
        t=0
        for k in range(8):
            t+=data[i+1+x[k]][j+1+y[k]]
        if t==3 or (t==2 and data[i+1][j+1]==1):
            ans[i][j]=1
for i in range(n):
    print(' '.join(map(str,ans[i])))