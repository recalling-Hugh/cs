import sys
t=int(sys.stdin.readline())
jump=[[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]
ans=0
def movef(r,chess,a,b):
    global ans
    if r==m*n:
        ans+=1
        return
    for i in range(8):
        if 0<=a+jump[i][0]<n and 0<=b+jump[i][1]<m:
            if chess[a+jump[i][0]][b+jump[i][1]]:
                chess[a+jump[i][0]][b+jump[i][1]]=False
                movef(r+1,chess,a+jump[i][0],b+jump[i][1])
                chess[a+jump[i][0]][b+jump[i][1]]=True
    return
for i in range(t):
    n, m, x, y = map(int, sys.stdin.readline().split())
    if (n==m and n==1) or (n>=3 and m>=3 and n*m!=9):
        board=[[True]*m for _ in range(n)]
        board[x][y]=False
        movef(1,board,x,y)
    print(ans)
    ans=0