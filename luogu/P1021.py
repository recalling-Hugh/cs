x=input().split()
n=int(x[0])
k=int(x[1])
f=[0]*20
b=[0]*20
ans=0
def testf(t):
    global ans
    global b
    if t==k:
        dp=[0]*5000
        i=0
        while dp[i]<=n:
            i+=1
            dp[i]=20
            for j in range(0,k):
                if i<f[j]:
                    break
                dp[i]=min(dp[i],dp[i-f[j]]+1)
        if i-1>ans:
            for j in range(0,k):
                b[j]=f[j]
                ans=i-1
        return
    for i in range(f[t-1]+1,f[t-1]*n+2):
        f[t]=i
        testf(t+1)
f[0]=1
testf(1)
a=''
for i in range(0,k):
    a=a+str(b[i])+' '
print(a)
print('MAX='+str(ans))
