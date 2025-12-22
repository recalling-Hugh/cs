import sys
n,d=map(int,sys.stdin.readline().split())
height=list(map(int,sys.stdin.read().split()))
result=[]
while height:
    m=len(height)
    index=[0]
    mn=height[0]
    mx=height[0]
    for i in range(1,m):
        h=height[i]
        if mx-d<=h<=mn+d:
            index.append(i)
        if h<mn:
            mn=h
        if h>mx:
            mx=h
    s=[height[i] for i in index]
    s.sort()
    result.extend(s)
    r=set(index)
    height=[height[i] for i in range(m) if i not in r]
print('\n'.join(map(str,result)))