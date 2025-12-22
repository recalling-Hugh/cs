c=input().split()
n=int(c[0])
m=int(c[1])
answer=0
for i in range(0,n):
    c=input().split()
    f=[]
    s=0
    f.append([])
    f[0].append(0)
    for i in range(1,m):
        f[0].append(f[0][i-1]+2**i*int(c[m-i]))
    for i in range(1,m):
        f.append([])
        f[i].append(f[i-1][0]+2**i*int(c[i-1]))
        for j in range(1,m):
            if i+j<=m-1:
                f[i].append(max((f[i-1][j]+2**(i+j)*int(c[i-1])),(f[i][j-1]+2**(i+j)*int(c[m-j]))))
            else:
                f[i].append(0)
    for i in range(0,m):
        if s<f[i][m-1-i]+2**m*int(c[i]):
            s=f[i][m-1-i]+2**m*int(c[i])
    answer+=s
print(answer)
