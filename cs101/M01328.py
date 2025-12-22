import sys
index=0
while True:
    index+=1
    data=list(map(int,sys.stdin.readline().split()))
    if data==[0,0]:
        break
    n=data[0]
    d=data[1]
    flag=True
    area=[]
    for i in range(n):
        data=list(map(int,sys.stdin.readline().split()))
        if data[1]>d:
            flag=False
        else:
            l=(d**2-data[1]**2)**0.5
            area.append([data[0]-l,data[0]+l])
    if flag:
        ans=0
        last=-10000
        area.sort(key=lambda x:x[1])
        for i in area:
            if i[0]>last:
                ans+=1
                last=i[1]
    else:
        ans=-1
    print('Case',str(index)+':',ans)
    sys.stdin.readline()