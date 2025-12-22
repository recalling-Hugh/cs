import math
a=[0]*6
data=[]
while True:
    data.append(list(map(int,input().split())))
    if data[-1]==a:
        data.pop(-1)
        break
for i in data:
    n=0
    n+=i[5]+i[4]+i[3]
    i[0]-=i[4]*11
    i[1]-=i[3]*5
    n+=math.ceil(i[2]/4)
    i[2]%=4
    if i[2]==3:
        i[1]-=1
        i[0]-=5
    elif i[2]==2:
        i[1]-=3
        i[0]-=6
    elif i[2]==1:
        i[1]-=5
        i[0]-=7
    if i[0]<=0:
        if i[1]>0:
            n+=math.ceil(i[1]/9)
    else:
        if i[1]<=0:
            i[0]+=i[1]*4
            if i[0]>0:
                n+=math.ceil(i[0]/36)
        else:
            n+=math.ceil(i[1]/9)
            i[1]%=9
            i[0]-=(9-i[1])*4
            n+=math.ceil(i[0]/36)
    print(n)