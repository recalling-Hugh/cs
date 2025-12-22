import sys
n=int(sys.stdin.readline())
data=[]
if n==1:
    ans=1
else:
    ans=2
    location=[]
    for i in range(n):
        data.append(list(map(int,sys.stdin.readline().split())))
        location.append([data[-1][0],data[-1][0]])
    for i in range(1,len(data)-1):
        if data[i][0]-data[i][1]>location[i-1][1]:
            location[i][0]-=data[i][1]
            ans+=1
            continue
        if data[i][0]+data[i][1]<location[i+1][0]:
            location[i][1]+=data[i][1]
            ans+=1
print(ans)