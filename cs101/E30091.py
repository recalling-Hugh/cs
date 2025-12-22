import sys
l=int(sys.stdin.readline())
n=int(sys.stdin.readline())
students=list(map(int,sys.stdin.readline().split()))
mn=0
mx=0
for i in students:
    if i<=l/2:
        mn=max(mn,i)
        mx=max(mx,l-i+1)
    else:
        mn=max(mn,l-i+1)
        mx=max(mx,i)
print(mn,mx)