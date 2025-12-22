n=int(input())
c=[]
for i in range(0,n):
    c.append(input().split())
t={}
for i in range(1,n):
    t[c[i][0]]=0
    for j in range(1,n):
        if len(c[i][j])==2:
            t[c[i][0]]+=1
flag=True
for i in range(1,n):
    for j in range(1,n):
        if len(c[i][j])==2:
            if t[c[i][j][0]]*(n-1)+t[c[i][j][1]]!=t[c[i][0]]+t[c[0][j]]:
                flag=False
        elif len(c[i][j])==1:
            if t[c[i][j]]!=t[c[i][0]]+t[c[0][j]]:
                flag=False
        else:
            flag=False
if flag:
    answer=''
    for i in range(1,n):
        answer=answer+c[i][0]+'='+str(t[c[i][0]])+' '
    print(answer)
    print(n-1)
else:
    print('ERROR!')
