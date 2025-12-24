import sys
n=int(sys.stdin.readline())
M=[]
flag={}
for i in range(n):
    M.append(list(map(int,sys.stdin.readline().split())))
    M[i].append(1)
    for j in range(n):
        flag[(i,j,True,True)]=True
        flag[(i,j,True,False)]=True
        flag[(i,j,False,True)]=True
        flag[(i,j,False,False)]=True
M.append([1]*(n+1))
def bfs(t,data):
    temp=[]
    global flag
    for i in data:
        if i[0]==n-1 and i[1]==n-2 and i[2]:
            return t
        if i[2]:
            if M[i[0]][i[1]+2]==0 and flag[(i[0],i[1]+1,True,True)]:
                temp.append((i[0],i[1]+1,True,True))
                flag[(i[0],i[1]+1,True,True)]=False
            if M[i[0]+1][i[1]]==0 and M[i[0]+1][i[1]+1]==0:
                if flag[(i[0]+1,i[1],True,True)]:
                    temp.append((i[0]+1,i[1],True,True))
                    flag[(i[0]+1,i[1],True,True)]=False
                if i[3] and flag[(i[0],i[1],False,False)]:
                    temp.append((i[0],i[1],False,False))
                    flag[(i[0],i[1],False,False)]=False
        else:
            if M[i[0]+2][i[1]]==0 and flag[(i[0]+1,i[1],False,True)]:
                temp.append((i[0]+1,i[1],False,True))
                flag[(i[0]+1,i[1],False,True)]=False
            if M[i[0]][i[1]+1]==0 and M[i[0]+1][i[1]+1]==0:
                if flag[(i[0],i[1]+1,False,True)]:
                    temp.append((i[0],i[1]+1,False,True))
                    flag[(i[0],i[1]+1,False,True)]=False
                if i[3] and flag[(i[0],i[1],True,False)]:
                    temp.append((i[0],i[1],True,False))
                    flag[(i[0],i[1],True,False)]=False
    temp=list(set(temp))
    if temp:
        return bfs(t+1,temp)
    else:
        return -1
s=bfs(0,[(0,0,True,True)])
print(s)