import sys
n,d=map(int,sys.stdin.readline().split())
height=list(map(int,sys.stdin.readline().split()))
height.sort()
flag=True
for i in range(0,2*n,2):
    if height[i+1]-height[i]>d:
        flag=False
        break
if flag:
    print('Yes')
else:
    print('No')