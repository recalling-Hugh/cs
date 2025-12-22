n=int(input())
if n%2==1:
    print(0,0)
else:
    mx=int(n/2)
    mn=0
    if n%4==0:
        mn=int(n/4)
    else:
        mn=int(n/4)+1
    print(mn,mx)