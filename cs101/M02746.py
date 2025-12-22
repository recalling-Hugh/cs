import sys
data=list(map(int,sys.stdin.readline().split()))
while data!=[0,0]:
    n=data[0]
    m=data[1]
    monkey=[]
    for i in range(n):
        monkey.append(i+1)
    while len(monkey)!=1:
        monkey.remove(monkey[m%len(monkey)-1])
        if m%(len(monkey)+1)!=0:
            monkey=monkey[m%(len(monkey)+1)-1:]+monkey[:m%(len(monkey)+1)-1]
    print(monkey[0])
    data=list(map(int,sys.stdin.readline().split()))