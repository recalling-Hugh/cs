n=int(input())
s=[]
for i in range(0,n):
    s.append([])
    for j in range(0,n):
        s[i].append(0)
data=[1,1,1]
while True:
    data=input().split()
    if data[0]=='0':
        break
    s[int(data[0])-1][int(data[1])-1]=int(data[2])
answer=[]
for i in range(0,2*n-1):
    answer.append([])
    for j in range(0,n):
        answer[i].append([])
        for k in range(0,n):
            answer[i][j].append(0)
for i in range(0,2*n-1):
    for j in range(max(0,i-n+1),min(i+1,n)):
        for k in range(max(0,i-n+1),min(i+1,n)):
            if j==k:
                answer[i][j][k]=max(answer[i-1][j][k],answer[i-1][j][k-1],answer[i-1][j-1][k-1],answer[i-1][j-1][k])+s[i-j][j]
            else:
                answer[i][j][k]=max(answer[i-1][j][k],answer[i-1][j][k-1],answer[i-1][j-1][k-1],answer[i-1][j-1][k])+s[i-j][j]+s[i-k][k]
print(answer[2*n-2][n-1][n-1])
