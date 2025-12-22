n=int(input().strip())
n%=26
s=input().strip()
ans=''
for i in s:
    m=ord(i)
    if 65<=m<=64+n or 97<=m<=96+n:
        ans+=chr(26+m-n)
    elif 65+n<=m<=90 or 97+n<=m<=122:
        ans+=chr(m-n)
print(ans)