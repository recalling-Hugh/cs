x=input().split()
p=int(x[0])
k=int(x[1])
search=[]
l=20*p
s=''
dp=[]
for i in range(0,l):
    dp.append([])
    for j in range(0,min(i+1,k)):
        dp[i].append(0)
for i in range(0,p):
    s+=input()
n=int(input())
dic=[]
for i in range(0,n):
    dic.append(input())
for i in range(0,l):
    for j in dic:
        if s[i:i+len(j)]==j:
            search.append([i,i+len(j)])
            break
for i in search:
    dp[i[1]-1][0]+=1
for i in range(1,l):
    dp[i][0]+=dp[i-1][0]
for i in range(1,l):
    for j in range(1,min(i,k)):
        b=0
        c=0
        if [i,i+1] in search:
            b=1
        for m in search:
            if m[1]==j:
                c+=1
        dp[i][j]=max(dp[i-1][j-1]+b,dp[i-1][j]+c)
print(dp[l-1][k-1])
