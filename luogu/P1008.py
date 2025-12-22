for i in range(123,330):
    a=[]
    a.append(int(i/100))
    a.append(int(i%100/10))
    a.append(int(i%10))
    a.append(int(2*i/100))
    a.append(int(2*i%100/10))
    a.append(int(2*i%10))
    a.append(int(3*i/100))
    a.append(int(3*i%100/10))
    a.append(int(3*i%10))
    s=0
    p=1
    for j in range(0,9):
        s+=a[j]
        p*=a[j]
    if s==45 and p==362880:
        print(str(i)+' '+str(2*i)+' '+str(3*i))
