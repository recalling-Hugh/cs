n=int(input())
data=[[],[],[],[]]
week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in range(0,n):
    data[0].append(input())
    data[1].append(int(data[0][i][2:4]))
    data[2].append(int(data[0][i][4:6]))
    data[3].append(int(data[0][i][6:8]))
    data[0][i]=int(data[0][i][0:2])
    print(week[(data[1][i]+int(data[1][i]/4)+int(data[0][i]/4)-2*data[0][i]+int(2.6*(data[2][i]+1))+data[3][i]-1)%7])