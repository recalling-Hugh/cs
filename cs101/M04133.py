import sys
m=[]
s=0
ans=0
for i in range(1025):
    m.append([0]*1025)
d=int(sys.stdin.readline())
n=int(sys.stdin.readline())
for i in range(n):
    data=list(map(int,sys.stdin.readline().split()))
    for j in range(max(0,data[0]-d),min(data[0]+d+1,1025)):
        for k in range(max(0,data[1]-d),min(data[1]+d+1,1025)):
            m[j][k]+=data[2]
            if m[j][k]==ans:
                s+=1
            elif m[j][k]>ans:
                ans=m[j][k]
                s=1
print(s,ans)