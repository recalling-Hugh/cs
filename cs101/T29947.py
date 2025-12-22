import sys
data=list(map(int,sys.stdin.readline().split()))
l=data[0]
m=data[1]
data=[]
k=[]
for i in range(m):
    data.append(list(map(int,sys.stdin.readline().split())))
data.sort()
for i in data:
    left=False
    inside=False
    for j in k:
        if i[1]<=j[1]:
            inside=True
            break
        if i[0]<=j[1]:
            left=j
    if inside:
        continue
    if left:
        left[1]=i[1]
    else:
        k.append(i)
ans=l+1
for i in k:
    ans-=(i[1]+1-i[0])
print(ans)