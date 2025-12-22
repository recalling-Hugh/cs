import sys
n,k=map(int,sys.stdin.readline().split())
coin=list(map(int,sys.stdin.readline().split()))
coin.sort()
if coin[0]!=1:
    print(-1)
else:
    x=0
    s=0
    while x<n:
        t=0
        for i in coin:
            if i<=x+1:
                t=i
            else:
                break
        x+=t
        s+=1
    print(s)