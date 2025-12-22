import sys
k=int(sys.stdin.readline())
dire=[[-1,0],[1,0],[0,-1],[0,1]]
def searchf(d,x,y,t):
    loc=[]
    for i in range(4):
        if t[x+dire[i][0]][y+dire[i][1]]==d:
            loc.append(dire[i])
            t[x+dire[i][0]][y+dire[i][1]]='#'
    for i in loc:
        searchf(d,x+i[0],y+i[1],t)
    return
for i in range(k):
    n=int(sys.stdin.readline())
    m=[['#']*(n+2)]
    r=0
    b=0
    for j in range(n):
        m.append(['#'])
        m[-1].extend(list(sys.stdin.readline()))
        m[-1].append('#')
    m.append(['#']*(n+2))
    for j in range(1,n+1):
        for l in range(1,n+1):
            if m[j][l]=='r':
                searchf('r',j,l,m)
                r+=1
            elif m[j][l]=='b':
                searchf('b',j,l,m)
                b+=1
    print(r,b)