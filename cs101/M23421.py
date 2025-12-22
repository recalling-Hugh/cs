import sys
n,b=map(int,sys.stdin.readline().split())
p=list(map(int,sys.stdin.readline().split()))
w=list(map(int,sys.stdin.readline().split()))
goods=[]
for i in range(n):
    goods.append((p[i],w[i]))
goods.sort(key=lambda x:x[1])
price=[0]*(b+1)
item=[]
for i in range(b+1):
    item.append([])
for i in range(b+1):
    j=0
    while goods[j][1]<=i:
        if price[i]<goods[j][0]+price[i-goods[j][1]] and j not in item[i-goods[j][1]]:
            price[i]=goods[j][0]+price[i-goods[j][1]]
            item[i]=[]
            item[i].extend(item[i-goods[j][1]])
            item[i].append(j)
        j+=1
        if j==n:
            break
    for j in range(i):
        if price[j]>price[i]:
            price[i]=price[j]
            item[i]=[]
            item[i].extend(item[j])
print(price[b])