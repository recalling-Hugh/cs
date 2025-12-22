import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
prime=[True]*1000001
prime[0]=False
prime[1]=False
for i in range(2,1001):
    for j in range(i*2,1000001,i):
        prime[j] = False
for i in data:
    if int(i**0.5)**2==i:
        t=int(i**0.5)
        if prime[t]:
            print('YES')
            continue
    print('NO')