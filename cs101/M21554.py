import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
index=[]
for i in range(n):
    index.append(i+1)
for i in range(n):
    for j in range(i+1,n):
        if data[i]>data[j]:
            index[i],index[j]=index[j],index[i]
            data[j],data[i]=data[i],data[j]
time=0
for i in range(n-1):
    if data[i]==data[i+1]:
        k=[]
        j=i
        while data[i]==data[j]:
            k.append(index[j])
            j+=1
            if j==len(data):
                break
        k.sort()
        index=index[:i]+k+index[j:]
for i in range(n):
    time+=(n-i-1)*data[i]
time/=n
print(' '.join(map(str,index)))
print('%.2f' %time)