def transferf(m,n):
    t=0
    if n!=16:
        for i in range(0,len(m)):
            t+=int(m[i])*n**(len(m)-1-i)
    else:
        number=['0','1','2','3','4','5','6','7','8','9']
        letter={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        for i in range(0,len(m)):
            if m[i] in number:
                t+=int(m[i])*n**(len(m)-1-i)
            else:
                t+=letter[m[i]]*n**(len(m)-1-i)
    return t
def decimalismf(t,n):
    m=''
    if n!=16:
        while t!=0:
            m+=str(t%n)
            t=int(t/n)
    else:
        letter={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while t!=0:
            if t%n<=9:
                m+=str(t%n)
                t=int(t/n)
            else:
                m+=letter[t%n]
                t=int(t/n)
    return m
n=int(input())
instr=input()
t=[]
for ch in instr:
    try:
        t.append(int(ch,base=n))
    except Exception:
        pass
m=''
if n!=16:
    for i in range(0,len(t)):
        m+=str(t[i])
else:
    letter={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    for i in range(0,len(t)):
        if t[i]<=9:
            m+=str(t[i])
        else:
            m+=letter[t[i]]
STEP=0
l=''
for i in range(len(m)-1,-1,-1):
    l+=(m[i])
while m!=l and STEP<=30:
    m=decimalismf(transferf(m,n)+transferf(l,n),n)
    l=''
    for i in range(len(m)-1,-1,-1):
        l+=(m[i])
    STEP+=1
if STEP==31:
    print('Impossible!')
else:
    print('STEP='+str(STEP))
