import sys
n=int(sys.stdin.readline())
coin=list(map(int,sys.stdin.readline().split()))
coin.sort(reverse=True)
s=0
for i in coin:
    s+=i
s/=2
ans=0
t=0
while t<=s:
    t+=coin[ans]
    ans+=1
print(ans)