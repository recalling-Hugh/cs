def movef(n):
    ans=2**n-1
    for i in range(1,n):
        ans=min(ans,2*movef(n-i)+2**i-1)
    return ans
for i in range(1,13):
    print(movef(i))