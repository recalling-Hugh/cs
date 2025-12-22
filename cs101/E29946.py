import sys
n=list(sys.stdin.readline().split()[0])
k=int(sys.stdin.readline())
t=0
ans=''
while k<len(n):
    mn=sorted(n[t:k+1])[0]
    ans+=mn
    for i in range(t,k+1):
        if n[i]==mn:
            t=i+1
            break
    k+=1
if list(ans)[0]=='0':
    temp=list(ans)
    while temp[0]=='0':
        del temp[0]
        if not temp:
            temp=['0']
            break
    ans=''
    for t in temp:
        ans+=t
print(ans)