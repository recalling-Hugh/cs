x=input().split()
n=int(x[0])
k=int(x[1])
ans=0
def dividef(a,t,l):
    global ans
    if t==1:
        ans+=1
        return
    for i in range(a,int(l/t)+1):
        dividef(i,t-1,l-i)
    return
for i in range(1,int(n/k)+1):
    dividef(i,k-1,n-i)
print(ans)
