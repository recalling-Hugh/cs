import sys
import copy
key=sys.stdin.readline().split()[0]
temp=list(key)
key=[]
for t in range(len(temp)):
    if temp[t]=='j':
        temp[t]='i'
    if temp[t] not in key:
        key.append(temp[t])
for i in range(97,123):
    if chr(i)=='j':
        continue
    if chr(i) not in key:
        key.append(chr(i))
alphabeta={}
matrix={}
for i in range(5):
    for j in range(i*5,(i+1)*5):
        alphabeta[key[j]]=(i,j-i*5)
        matrix[(i,j-i*5)]=key[j]
for i in range(5):
    matrix[(i,5)]=matrix[(i,0)]
    matrix[(5,i)]=matrix[(0,i)]
n=int(sys.stdin.readline())
for i in range(n):
    code=sys.stdin.readline().split()[0]
    temp=list(code)
    t=0
    while t<len(temp):
        if temp[t]=='j':
            temp[t]='i'
        t+=1
    code=copy.deepcopy(temp)
    j=0
    while j<len(code):
        if j==len(code)-1:
            if code[j]=='x':
                code.append('q')
            else:
                code.append('x')
        else:
            if code[j]==code[j+1]:
                if code[j]=='x':
                    code=code[:j+1]+['q']+code[j+1:]
                else:
                    code=code[:j+1]+['x']+code[j+1:]
        if alphabeta[code[j]][0]==alphabeta[code[j+1]][0]:
            code[j]=matrix[(alphabeta[code[j]][0],alphabeta[code[j]][1]+1)]
            code[j+1]=matrix[(alphabeta[code[j+1]][0],alphabeta[code[j+1]][1]+1)]
        elif alphabeta[code[j]][1]==alphabeta[code[j+1]][1]:
            code[j]=matrix[(alphabeta[code[j]][0]+1,alphabeta[code[j]][1])]
            code[j+1]=matrix[(alphabeta[code[j+1]][0]+1,alphabeta[code[j+1]][1])]
        else:
            temp=code[j]
            code[j]=matrix[(alphabeta[code[j]][0],alphabeta[code[j+1]][1])]
            code[j+1]=matrix[(alphabeta[code[j+1]][0],alphabeta[temp][1])]
        j+=2
    print(''.join(code))