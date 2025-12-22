import sys
data=list(map(int,sys.stdin.read().split()))
a=data[0]
b=data[1]+1
data=[]
for i in range(a,b):
    p=i//100
    q=i%100//10
    s=i%10
    if i==p**3+q**3+s**3:
        data.append(i)
ans=''
if len(data)>0:
    for i in data:
        ans+=str(i)+' '
    ans=ans[:-1]
else:
    ans='NO'
print(ans)