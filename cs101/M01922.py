import sys
import math
def ridef(t,r,start_i):
    while True:
        t_min=10000
        temp=-1
        for i in range(start_i,len(r)):
            if r[i][0]==r[start_i][0]:
                continue
            time_val=(r[start_i][2]-r[i][2])*3.6/(r[i][0]-r[start_i][0])
            if 0<=time_val<=t_min:
                t_min=time_val
                temp=i
        if temp==-1 or t_min*r[start_i][0]/3.6+r[start_i][2]>=4500:
            return (4500-r[start_i][2])*3.6/(r[start_i][0])+t
        for i in range(temp,len(r)):
            r[i][2]+=t_min*r[i][0]/3.6
        t+=t_min
        start_i=temp
data=[]
for line in sys.stdin:
    data.append(line)
n=int(data[0])
k=1
while n!=0:
    t_min=0
    rider=[list(map(float,data[i+k].split())) for i in range(n)]
    rider.sort(key=lambda x:(x[0],-x[1]))
    for i in range(n):
        rider[i].append(-rider[i][0]*rider[i][1]/3.6)
        if 0<=rider[i][1]<rider[t_min][1] or rider[t_min][1]<0<=rider[i][1]:
            t_min=i
        elif rider[i][1]==rider[t_min][1]:
            if rider[i][0]>rider[t_min][0]:
                t_min=i
    print(math.ceil(round(ridef(0,rider,t_min),6)))
    k+=n+1
    n=int(data[k-1])