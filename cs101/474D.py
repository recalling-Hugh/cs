import sys
n,k=map(int,sys.stdin.readline().split())
data=[]
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
data_1=sorted(data,key=lambda x:x[1])
dp=[1]*(data_1[-1][1]+1)
ans=[0]*(data_1[-1][1]+1)
for i in range(1,k):
    ans[i]=ans[i-1]+dp[i]
for i in range(k,data_1[-1][1]+1):
    dp[i]=(dp[i-k]+dp[i-1])%1000000007
    ans[i]=(ans[i-1]+dp[i])%1000000007
for i in range(n):
    print((ans[data[i][1]]-ans[data[i][0]-1])%1000000007)