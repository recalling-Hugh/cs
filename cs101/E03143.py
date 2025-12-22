n=int(input())
if n%2==1 or n<6:
    print('Error!')
else:
    p=[2]
    for i in range(3,n,2):
        flag=True
        for j in p:
            if i%j==0:
                flag=False
                break
        if flag:
            p.append(i)
    for i in range(3,int(n/2)+1,2):
        if i in p and (n-i) in p:
            print('%d=%d+%d'%(n,i,n-i))