import sys
data=list(map(int,sys.stdin.readline().split()))
n=data[0]
m=data[1]
data=[]
s=0
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
    data[i].append(data[i][0]/data[i][1])
data.sort(key=lambda x:x[2],reverse=True)
for i in data:
    if m<i[1]:
        s+=i[2]*m
        break
    s+=i[0]
    m-=i[1]
print('%.2f' % s)