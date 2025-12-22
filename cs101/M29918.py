n=int(input())
s=[0]*(n+1)
for i in range(1,n//2+1):
    for j in range(2*i,n+1,i):
        s[j]+=i
for i in range(n):
    if s[i]<=n:
        if s[s[i]]==i and i<s[i]:
            print(i,s[i])