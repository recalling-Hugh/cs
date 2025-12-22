n=int(input())
s=0
for i in range(1,10000):
    s+=i
    if s>=n:
        s-=i
        n-=s
        if i%2==0:
            print(str(n)+'/'+str(i+1-n))
        else:
            print(str(i+1-n)+'/'+str(n))
        break
