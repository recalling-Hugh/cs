import sys
t=int(sys.stdin.readline())
for _ in range(t):
    l,r,x=map(int,sys.stdin.readline().split())
    a,b=map(int,sys.stdin.readline().split())
    ans=-1
    flag=[a-l>=x,r-a>=x,b-l>=x,r-b>=x]
    if a==b:
        ans=0
    if (flag[0] or flag[1]) and (flag[2] or flag[3]):
        if abs(a-b)>=x:
            ans=1
        elif (flag[0] and flag[2]) or (flag[1] and flag[3]):
            ans=2
        else:
            ans=3
    print(ans)