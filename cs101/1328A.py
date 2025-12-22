import math
n=int(input())
for i in range(n):
    data=list(map(int,input().split()))
    print(math.ceil(data[0]/data[1])*data[1]-data[0])