import sys
data=list(map(float,sys.stdin.read().splitlines()))
for i in data:
    j=1
    j1=1
    n=0
    while True:
        j=j1
        j1=j-(j**2-i)/(2*j)
        n+=1
        if abs(j1-j)<=0.000001:
            break
    print('%d %.2f'%(n,j1))