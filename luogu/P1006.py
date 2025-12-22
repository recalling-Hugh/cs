c=input().split()
m=int(c[0])
n=int(c[1])
s=[]
for i in range(0,m):
    s.append(input().split())
answer=[]
for i in range(0,m+n-1):
    answer.append([])
    for j in range(0,m):
        answer[i].append([])
        for k in range(0,m):
            answer[i][j].append(0)
for i in range(0,m+n-2):
    for j in range(max(0,i-n+1),min(i+1,m)):
        for k in range(max(0,i-n+1),min(i+1,m)):
            if j!=k:
                answer[i][j][k]=max(answer[i-1][j][k],answer[i-1][j-1][k],answer[i-1][j][k-1],answer[i-1][j-1][k-1])+int(s[j][i-j])+int(s[k][i-k])
print(max(answer[m+n-3][m-2][m-1],answer[m+n-3][m-1][m-2]))
