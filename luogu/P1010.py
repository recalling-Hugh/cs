def calculatef(n,s):
    b=[]
    while n !=0:
        b.append(n%2)
        n=int(n/2)
    flag=True
    if len(b)<=2:
        flag=False
    while len(b)>2:
        s+='2('
        s=calculatef(len(b)-1,s)
        b.pop()
        if len(b)>0:
            while b[-1]==0 and len(b)>2:
                b.pop()
                if len(b)==0:
                    break
        s+=')+'
    if flag:
        if b[0]==1:
            if b[1]==1:
                s+='2+2(0)'
            else:
                s+='2(0)'
        elif b[1]==1:
            s+='2'
        else:
            s=s[:-1]
    else:
        if b[0]==1:
            if b[1]==1:
                s+='2+2(0)'
            else:
                s+='2(0)'
        else:
            s+='2'
    return s
n=int(input())
s=''
s=calculatef(n,s)
print(s)
