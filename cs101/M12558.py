import sys
data=list(map(int,sys.stdin.readline().split()))
m=data[0]
n=data[1]
island=[]
for i in range(m):
    island.append(list(map(int,sys.stdin.readline().split())))
if m==1 or n==1:
    ans=0
    for i in range(m):
        for j in range(n):
            ans+=island[i][j]
    ans=2*ans+2
    print(ans)
else:
    ans=(4-island[0][1]-island[1][0])*island[0][0]
    ans+=(4-island[0][n-2]-island[1][n-1])*island[0][n-1]
    ans+=(4-island[m-2][0]-island[m-1][1])*island[m-1][0]
    ans+=(4-island[m-2][n-1]-island[m-1][n-2])*island[m-1][n-1]
    for i in range(1,n-1):
        ans+=(4-island[0][i-1]-island[0][i+1]-island[1][i])*island[0][i]
        ans+=(4-island[m-1][i-1]-island[m-1][i+1]-island[m-2][i])*island[m-1][i]
        for j in range(1,m-1):
            ans+=(4-island[j-1][i]-island[j+1][i]-island[j][i-1]-island[j][i+1])*island[j][i]
    for i in range(1,m-1):
        ans+=(4-island[i-1][0]-island[i+1][0]-island[i][1])*island[i][0]
        ans+=(4-island[i-1][n-1]-island[i+1][n-1]-island[i][n-2])*island[i][n-1]
    print(ans)