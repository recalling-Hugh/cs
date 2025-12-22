day=[]
for i in range(0,15):
    day.append([])
    for j in range(0,40):
        day[i].append([])
n=int(input())
for i in range(0,n):
    data=input().split()
    data[1]=int(data[1])
    data[2]=int(data[2])
    day[data[1]][data[2]].append(data[0])
for i in range(0,13):
    for j in range(0,32):
        if len(day[i][j])>1:
            ans=str(i)+' '+str(j)
            for k in day[i][j]:
                ans+=' '+str(k)
            print(ans)
