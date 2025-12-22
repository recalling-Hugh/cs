a=[]
b=[]
while True:
    a.append(float(input()))
    if a[-1]==0:
        a.pop(-1)
        break
    b.append(0)
i=1
c=0
while 0 in b:
    c+=1/(i+1)
    for j in range(0,len(a)):
        if a[j]<c and b[j]==0:
            b[j]=i
    i+=1
for j in b:
    print(str(j)+' card(s)')
