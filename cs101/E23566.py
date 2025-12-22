data=list(map(int,input().split()))
n=data[0]
m=data[1]
num=[0]*m
s=0
for i in range(0,n):
    data=list(map(int,input().split()))
    num[data[0]-1]+=data[1]
    s+=data[1]
s-=int(s/200)*30
for i in range(0,m):
    flag=True
    data=input()
    p=0
    q=0
    for j in data:
        if j=='-':
            flag=False
        elif flag:
            p=p*10+int(j)
        else:
            q=q*10+int(j)
    if num[i]>=p:
        s-=q
print(s)
