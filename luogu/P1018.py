s=input().split()
n=int(s[0])
k=int(s[1])
s=input()
dp=[[]]
for i in range(0,n):
    dp[0].append(int(s[0:i+1]))
for i in range(0,k):
    dp.append([])
    most=0
    for j in range(0,n-i-1):
        for m in range(0,j+1):
            if most<dp[i][m]*int(s[i+m+1:i+j+2]):
                most=dp[i][m]*int(s[i+m+1:i+j+2])
        dp[i+1].append(most)
print(dp[k][n-k-1])
