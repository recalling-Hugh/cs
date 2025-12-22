import sys
a=int(sys.stdin.readline())
dire=[[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1]]
def area(x,y,t):
    s=1
    for i in range(8):
        if t[x+dire[i][0]][y+dire[i][1]]=='W':
            t[x+dire[i][0]][y+dire[i][1]]='.'
            s+=area(x+dire[i][0],y+dire[i][1],t)
    return s
for i in range(a):
    ans=0
    m,n=map(int,sys.stdin.readline().split())
    dotmap=[['.']*(n+2)]
    for j in range(m):
        dotmap.append(['.'])
        dotmap[-1].extend(list(sys.stdin.readline()))
        dotmap[-1].extend(['.'])
    dotmap.append(['.']*(n+2))
    for j in range(1,m+1):
        for k in range(1,n+1):
            if dotmap[j][k]=='W':
                dotmap[j][k]='.'
                ans=max(area(j,k,dotmap),ans)
    print(ans)