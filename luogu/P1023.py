n=int(input())
d=[[0,0]]
while d[-1][0]!='-1':
    d.append(input().split())
t=int(input())
d.pop(-1)
d.pop(0)
k=int(d[0][0])
n-=k
for i in d:
    i[0]=int(i[0])-k
    i[1]=int(i[1])
f=0
while f<len(d)-1:
    if d[f][0]!=d[f+1][0]-1:
        p=d[f+1][0]-d[f][0]
        k=(d[f+1][1]-d[f][1])/p
        for j in range(1,p):
            d.insert(f+j,[d[f][0]+j,d[f][1]+j*k])
    f+=1
while d[-1][1]>0:
    d.append([d[-1][0]+1,d[-1][1]-t])
d.pop(-1)
if n>=len(d):
    print('NO SOLUTION')
else:
    i=1
    while True:
        target=(i+n)*d[n][1]
        flag=True
        for j in range(0,len(d)):
            k=(i+j)*d[j][1]
            if k>target:
                flag=False
                break
        if flag:
            print(i)
            break
        i=-i
        target=(i+n)*d[n][1]
        flag=True
        for j in range(0,len(d)):
            k=(i+j)*d[j][1]
            if k>target:
                flag=False
                break
        if flag:
            print(i)
            break
        i=1-i
