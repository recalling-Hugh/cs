import sys
m=[]
n=int(sys.stdin.readline())
for i in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))
INF=float('inf')
dp=[[INF]*n for _ in range(1<<n)]
dp[1][0]=0
for t in range(1<<n):
    for i in range(n):
        if dp[t][i]==INF:
            continue
        for j in range(n):
            if t>>j&1:
                continue
            new=t|(1<<j)
            dp[new][j]=min(dp[new][j],dp[t][i]+m[i][j])
ans=INF
for i in range(1,n):
    ans=min(ans,dp[(1<<n)-1][i]+m[i][0])
print(ans)