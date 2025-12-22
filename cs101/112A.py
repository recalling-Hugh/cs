a=input()
b=input()
ans=0
for i in range(0,len(a)):
    A=ord(a[i])
    B=ord(b[i])
    if 65<=A<=90:
        A+=32
    if 65<=B<=90:
        B+=32
    if A<B:
        ans=-1
        break
    if A>B:
        ans=1
        break
print(ans)