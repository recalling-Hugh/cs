import sys
n=int(sys.stdin.readline())
onion=[]
for i in range(n):
    onion.append(list(map(int,sys.stdin.readline().split())))
tear=(n+1)//2
page=[0]*tear
if n%2==0:
    for i in range(tear):
        for j in range(i,n-i-1):
            page[i]+=onion[i][j]+onion[j+1][i]+onion[n-i-1][j+1]+onion[j][n-1-i]
else:
    for i in range(tear-1):
        for j in range(i,n-i-1):
            page[i]+=onion[i][j]+onion[j+1][i]+onion[n-i-1][j+1]+onion[j][n-1-i]
    page[tear-1]=onion[tear-1][tear-1]
page.sort()
print(page[-1])