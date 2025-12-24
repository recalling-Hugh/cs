import sys
n,m=map(int,sys.stdin.readline().split())
price=list(map(int,sys.stdin.readline().split()))
price.sort()
fruit={}
for i in range(m):
    f=sys.stdin.readline().split()
    if f[0] not in fruit.keys():
        fruit[f[0]]=1
    else:
        fruit[f[0]]+=1
number=list(fruit.values())
number.sort(reverse=True)
mn=mx=0
for i in range(len(number)):
    mn+=number[i]*price[i]
    mx+=number[i]*price[n-1-i]
print(mn,mx)