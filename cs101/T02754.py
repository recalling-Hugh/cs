import sys
import copy
queen=[]
def changef(x,y,c):
    b=copy.deepcopy(c)
    for i in range(8):
        b[x][i]=False
        b[i][y]=False
    for i in range(max(0,x+y-7),min(8,x+y+1)):
        b[i][x+y-i]=False
    for i in range(max(-x,-y),min(8-x,8-y)):
        b[x+i][y+i]=False
    return b
def dancef(x,c,s):
    b=copy.deepcopy(c)
    if x==7:
        for i in range(8):
            if b[x][i]:
                s=10*s+i+1
                queen.append(s)
                return
    for i in range(8):
        if b[x][i]:
            s=10*s+i+1
            d=changef(x,i,b)
            dancef(x+1,d,s)
            s=int(s/10)
    return
n=int(sys.stdin.readline())
board=[]
for i in range(8):
    board.append([True]*8)
dancef(0,board,0)
for i in range(n):
    print(queen[int(sys.stdin.readline())-1])