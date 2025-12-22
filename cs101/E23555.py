import sys
data=list(map(int,sys.stdin.readline().split()))
n=data[0]
m_1=data[1]
m_2=data[2]
matrix_a={}
matrix_b={}
for i in range(n):
    matrix_a[i]=[]
    matrix_b[i]=[]
for i in range(m_1):
    data=list(map(int,sys.stdin.readline().split()))
    matrix_a[data[1]].append((data[0],data[2]))
for i in range(m_2):
    data=list(map(int,sys.stdin.readline().split()))
    matrix_b[data[0]].append((data[1],data[2]))
ans=[]
for i in range(n):
    ans.append([0]*n)
for i in range(n):
    for j in matrix_a[i]:
        for k in matrix_b[i]:
            ans[j[0]][k[0]]+=j[1]*k[1]
for i in range(n):
    for j in range(n):
        if ans[i][j]!=0:
            print(' '.join(map(str,[i,j,ans[i][j]])))