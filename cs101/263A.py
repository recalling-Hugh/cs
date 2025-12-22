import sys
x=0
y=0
data=sys.stdin.read().splitlines()
for i in range(5):
    data[i]=data[i].split()
    for j in range(5):
        if data[i][j]=='1':
            x=i
            y=j
            break
print(abs(2-x)+abs(2-y))