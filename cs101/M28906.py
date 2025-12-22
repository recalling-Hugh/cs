import sys
n,k=map(int,sys.stdin.readline().split())
def dividef(m,j,l):
    if j==1:
        return 1
    s=0
    for i in range(l-1,m//j):
        s+=dividef(m-i-1,j-1,i+1)
    return s
print(dividef(n,k,1))