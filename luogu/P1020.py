import math
s=input().split()
f=[0]*(len(s)+1)
f[0]=1000000000000
quantity=0
def searchf(l,r,n,t,b):
    if r-l==1:
        return r
    if b:
        if t[int((l+r)/2)]>=n:
            return searchf(int((l+r)/2),r,n,t,b)
        else:
            return searchf(l,int((l+r)/2),n,t,b)
    else:
        if t[int((l+r)/2)]<n:
            return searchf(int((l+r)/2),r,n,t,b)
        else:
            return searchf(l,int((l+r)/2),n,t,b)
for i in s:
    if f[quantity]>=int(i):
        quantity+=1
        f[quantity]=int(i)
    else:
        f[searchf(0,quantity,int(i),f,True)]=int(i)
print(quantity)
p=[0]
batch=0
for i in s:
    if p[-1]<int(i):
        batch+=1
        p.append(int(i))
    else:
        p[searchf(0,batch,int(i),p,False)]=int(i)
    print(p)
print(batch)
