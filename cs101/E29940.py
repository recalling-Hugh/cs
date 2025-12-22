n=int(input())
a=list(map(int,input().split()))
mn=0
s=0
for i in a:
    s+=i
    mn=min(mn,s)
print(1-mn)