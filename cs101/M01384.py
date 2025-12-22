import sys
t=int(sys.stdin.readline())
for _ in range(t):
    before,after=map(int,sys.stdin.readline().split())
    weight=after-before
    n=int(sys.stdin.readline())
    piggy=[]
    package=[10000000]*(weight+1)
    for _ in range(n):
        piggy.append(list(map(int,sys.stdin.readline().split())))
    if n==1:
        if piggy[0][1]<=weight:
            package[piggy[0][1]]=piggy[0][0]
    else:
        if piggy[-1][1]!=piggy[-2][1] and piggy[-1][1]<=weight:
            package[piggy[-1][1]]=piggy[-1][0]
    piggy.sort(key=lambda x:x[1])
    i=0
    while i<len(piggy)-1:
        if piggy[i][1]==piggy[i+1][1]:
            piggy[i][0]=min(piggy[i][0],piggy[i+1][0])
            del piggy[i+1]
        else:
            if piggy[i][1]<=weight:
                package[piggy[i][1]]=piggy[i][0]
            i+=1
    for i in range(weight+1):
        for j in piggy:
            if i<=j[1]:
                break
            package[i]=min(package[i],package[i-j[1]]+j[0])
    if package[weight]==10000000:
        if weight!=0:
            print('This is impossible.')
        else:
            print('The minimum amount of money in the piggy-bank is 0.')
    else:
        print(f'The minimum amount of money in the piggy-bank is {package[weight]}.')