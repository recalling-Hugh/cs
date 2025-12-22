import sys
n=int(sys.stdin.readline())
ans=1
nums=list(map(int,sys.stdin.readline().split()))
positive=[1]*n
negative=[1]*n
for i in range(n):
    for j in range(i):
        if nums[i]>nums[j]:
            positive[i]=max(negative[j]+1,positive[i])
            ans=max(ans, positive[i])
        elif nums[i]<nums[j]:
            negative[i]=max(positive[j]+1,negative[i])
            ans=max(ans, negative[i])
print(ans)