import sys
data=sys.stdin.read().split(',')
data[2]=data[2].replace('\n','')
m,n,k=map(int,data)
t=len(str(n))
mx=((n+1)//(10**(t-1))-1)+9*(t-1)
mx=mx//k
ans=[]
for i in range(mx):
    ans.append([])
for i in range(m+1,n):
    s=i//1000+i%1000//100+i%100//10+i%10
    if s%k==0:
        ans[s//k-1].append(i)
for i in ans:
    if i:
        print(','.join([str(j) for j in i]))