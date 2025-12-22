n=int(input())
ans=0
for i in range(1,n+1):
    if i%7!=0 and i%10!=7 and int(i/10)!=7:
        ans+=i**2
print(ans)
