import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.read().split()))
matrix=[]
for i in range(n):
    matrix.append(data[i*n:(i+1)*n])
def kadane(up,down):
    data=[0]*n
    for i in range(n):
        for j in range(up,down+1):
            data[i]+=matrix[j][i]
    now=data[0]
    s=data[0]
    for i in range(1,n):
        now=max(now+data[i],data[i])
        s=max(s,now)
    return s
ans=matrix[0][0]
for i in range(n):
    for j in range(i+1,n):
        ans=max(ans,kadane(i,j))
print(ans)