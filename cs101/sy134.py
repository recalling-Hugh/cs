import sys
import copy
result=[]
def arrangef(ans,num,index):
    if num==[0]*110:
        result.append(ans)
        return
    for i in index:
        if num[i]!=0:
            num[i]-=1
            ans_1=copy.deepcopy(ans)
            ans_1.append(i)
            arrangef(ans_1,num,index)
            num[i]+=1
    return
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
num=[0]*110
for i in data:
    num[i]+=1
index=sorted(set(data))
arrangef([],num,index)
result=[list(item) for item in set(tuple(sublist) for sublist in result)]
result.sort()
for i in result:
    print(' '.join(map(str,i)))