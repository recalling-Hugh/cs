n=int(input())
s=[[],[],[]]
def linef(b,t,l):
    l+=1
    flag=True
    most=0
    for c in s[2][t]:
        if b[c[0]]==2:
            continue
        b[c[0]]+=1
        most=max(most,s[1][t]-c[1]+linef(b,c[0],l))
        b[c[0]]-=1
        flag=False
    if flag:
        return s[1][t]
    else:
        return most
for i in range(0,n):
    s[0].append(input().rstrip())
    s[1].append(len(s[0][i]))
    s[2].append([])         #s[0]记录字符串，s[1]记录字符串长度，s[2]记录可接龙及重叠
    for j in range(0,i):
        for k in range(s[1][j]-1,max(0,s[1][j]-s[1][i]),-1):
            if s[0][j][k:]==s[0][i][0:s[1][j]-k]:
                s[2][j].append([i,s[1][j]-k])
                break
        for k in range(s[1][i]-1,max(0,s[1][i]-s[1][j]),-1):
            if s[0][i][k:]==s[0][j][0:s[1][i]-k]:
                s[2][i].append([j,s[1][i]-k])
                break
    for j in range(s[1][i]-1,0,-1):
        if s[0][i][j:]==s[0][i][:s[1][i]-j]:
            s[2][i].append([i,s[1][i]-j])
b=[0]*n
answer=0
start=input().rstrip()
for i in range(0,n):
    if s[0][i][0]!=start:
        continue
    b[i]+=1
    answer=max(answer,linef(b,i,0))
    b[i]-=1
print(answer)
