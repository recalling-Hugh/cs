import sys
coefficient=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
tail=['1','0','X','9','8','7','6','5','4','3','2']
data=sys.stdin.read().splitlines()
n=int(data[0])
for i in range(1,n+1):
    s=0
    for j in range(0,17):
        s+=int(data[i][j])*coefficient[j]
    s%=11
    if data[i][17]==tail[s]:
        print('YES')
    else:
        print('NO')