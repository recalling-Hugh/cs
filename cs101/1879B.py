import sys
s=int(sys.stdin.readline())
for i in range(s):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    b=list(map(int,sys.stdin.readline().split()))
    a.sort()
    b.sort()
    r=n*b[0]
    t=n*a[0]
    for j in range(n):
        r+=a[j]
        t+=b[j]
    print(min(r,t))