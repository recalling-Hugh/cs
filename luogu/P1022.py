q=input().strip()
t=[0]
b=[True]
bug=[]
negative=[not((q[0]=='-')^True)]
flag=True
p=False
unknown=''
number=['0','1','2','3','4','5','6','7','8','9']
symbol=['-','+']
i=0
m=0
l=0
if q[0] not in number and q[0] not in symbol and q[0]!='=':
    q='1'+q
for c in range(1,len(q)):
    if q[c] not in number and q[c] not in symbol and q[c]!='=':
        unknown=q[c]
        if q[c-1] not in number:
            bug.append(c)
bug.append(len(q))
f=q[0:bug[0]]
for c in range(0,len(bug)-1):
    f=f+'1'+unknown+q[bug[c]+1:bug[c+1]]
for c in f:
    if p:
        p=False
        if c in number:
            t.append(0)
            b.append(True)
            negative.append(True)
            i+=1
    if c not in number and c not in symbol and c!='=':
        if len(t)!=i+1:
            t[i].append(1)
            b[i].append(False)
        else:
            b[i]=False
    elif c in number:
        t[i]=t[i]*10+int(c)
    elif c in symbol:
        t.append(0)
        b.append(True)
        negative.append(not((c=='-')^flag))
        i+=1
    else:
        flag=False
        p=True
for j in range(0,i+1):
    if b[j]:
        if negative[j]:
            m+=t[j]
        else:
            m-=t[j]
    else:
        if negative[j]:
            l+=t[j]
        else:
            l-=t[j]
s=round(-m/l,3)
answer=f'{s:.3f}'
print(unknown+'='+answer)
