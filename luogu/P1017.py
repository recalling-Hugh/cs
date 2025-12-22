s=input().split()
m=int(s[0])
n=int(s[1])
letter={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J'}
answer=''
m_1=m
if m!=0:
    while m_1!=0:
        if m_1%n==0:
            k=0
        else:
            k=m_1%n-n
        if k<=9:
            answer=str(k)+answer
        else:
            answer=letter[k]+answer
        m_1=int((m_1-k)/n)
else:
    answer='0'
print(str(m)+'='+answer+'(base'+str(n)+')')
