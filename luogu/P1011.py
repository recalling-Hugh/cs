s=input().split()
a=int(s[0])
n=int(s[1])
m=int(s[2])
x=int(s[3])
if n==2:
    print(a)
else:
    a1=[1,1]
    a2=[1,0]
    b1=[0,0]
    b2=[0,1]
    for i in range(2,n-1):
        a2.append(a2[i-1]+a2[i-2])
        b2.append(b2[i-1]+b2[i-2])
        a1.append(a1[i-1]+a2[i-2])
        b1.append(b1[i-1]+b2[i-2])
    b=(m-a1[n-2]*a)/b1[n-2]
    print(int(a1[x-1]*a+b1[x-1]*b))
