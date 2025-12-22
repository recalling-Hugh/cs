n=int(input())
ans=''
while n!=0:
    ans=str(n%8)+ans
    n=int(n/8)
print(ans)
