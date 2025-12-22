f=input().split()
c=float(f[1])
k=float(f[2])
n=int(f[4])
answer=0
d=[]
d.append([])
d[0].append(0.0)
d[0].append(float(f[3]))
for i in range(0,n):
    q=input().split()
    d.append([])
    d[i+1].append(float(q[0]))
    d[i+1].append(float(q[1]))
most=c*k
for i in range(1,n+1):
    for j in range(1,i):
        if d[i][0]<d[j][0]:
            d[i][0],d[j][0]=d[j][0],d[i][0]
            d[i][1],d[j][1]=d[j][1],d[i][1]
d.append([])
d[n+1].append(float(f[0]))
d[n+1].append(0.0)
flag=True
for i in range(0,n+1):
    if d[i+1][0]-d[i][0]>most:
        flag=False
        print('No Solution')
        break
if flag:
    location=0
    left=0
    least=[0,0]
    while location!=n+1:
        least[0]=location+1
        least[1]=d[location+1][1]
        for i in range(location+1,n+2):
            if d[i][0]>d[location][0]+most:
                answer+=(c-left)*d[location][1]
                left=c-(d[least[0]][0]-d[location][0])/k
                location=least[0]
                break
            if least[1]>=d[i][1]:
                least[0]=i
                least[1]=d[i][1]
            if d[i][1]<=d[location][1]:
                answer+=((d[i][0]-d[location][0])/k-left)*d[location][1]
                location=i
                left=0
                break
    print('{:.2f}'.format(round(answer,2)))
