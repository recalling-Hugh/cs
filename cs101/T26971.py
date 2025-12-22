import sys
n=int(sys.stdin.readline())
rating=list(map(int,sys.stdin.readline().split()))
up=[]
down=[]
start=0
ans=0
i=0
while i<len(rating)-1:
    if rating[i]==rating[i+1]:
        ans+=1
        del rating[0]
    elif rating[i]<rating[i+1]:
        flag=1
        up.append([i,i+1])
        start=i
        break
    else:
        flag=-1
        down.append([i,i+1])
        start=i
        break
    i+=1
if len(rating)!=1:
    while rating[-1]==rating[-2]:
        ans+=1
        del rating[-1]
        if len(rating)==1:
            break
n=len(rating)
for i in range(n-1):
    if rating[i]==rating[i+1]:
        flag=0
        continue
    if rating[i]>rating[i+1]:
        if flag!=-1:
            down.append([i,i+1])
            flag=-1
        else:
            down[-1][1]=i+1
    else:
        if flag==1:
            up[-1][1]=i+1
        else:
            up.append([i,i+1])
            flag=1
candy=[1]*n
for i in up:
    for j in range(i[0],i[1]+1):
        candy[j]=j-i[0]+1
for i in down:
    for j in range(i[1],i[0]-1,-1):
        candy[j]=max(candy[j],i[1]-j+1)
for i in candy:
    ans+=i
print(ans)