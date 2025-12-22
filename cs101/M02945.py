import sys
m=int(sys.stdin.readline())
s=list(map(int,sys.stdin.readline().split()))
f=[0]*(m+1)
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
    if f[quantity]>=i:
        quantity+=1
        f[quantity]=i
    else:
        f[searchf(0,quantity,i,f,True)]=i
print(quantity)