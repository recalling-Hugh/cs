import sys
n=int(sys.stdin.readline())
data=[0,1,2]
for i in range(2,n):
    data.append(data[-1]+data[-2])
print(data[n])