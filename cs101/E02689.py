s=input()
ans=''
for i in s:
    if 65<=ord(i)<=90:
        ans+=chr(ord(i)+32)
    elif 97<=ord(i)<=122:
        ans+=chr(ord(i)-32)
    else:
        ans+=i
print(ans)
