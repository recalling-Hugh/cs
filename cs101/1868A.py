import sys
s=int(sys.stdin.readline())
for i in range(s):
    n,m=map(int,sys.stdin.readline().split())
    if m==1:
        for i in range(n+1):
            print(0)
    elif n>=m-1:
        print(m)
        data=[]
        for j in range(m-1):
            data.append([])
            for k in range(m):
                data[j].append((j+k)%m)
        for j in range(n):
            print(' '.join(map(str,data[j%(m-1)])))
    else:
        print(n+1)
        data=[]
        for j in range(n):
            data.append([])
            for k in range(m):
                data[j].append((j+k)%m)
            print(' '.join(map(str,data[j%(m-1)])))