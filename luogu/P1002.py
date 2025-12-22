s=input().split()
n=int(s[0])
m=int(s[1])
p=int(s[2])
q=int(s[3])
table=[]
for i in range(0,n+1):
    table.append([])
    for j in range(0,m+1):
        table[i].append(0)
if (p!=0 or q!=0) and (p!=2 or q!=1) and (p!=1 or q!=2):
    table[0][0]=1
for i in range(0,n+1):
    for j in range(0,m+1):
        if (i!=0 or j!=0) and (i!=p or j!=q) and ((i!=p+2 and i!=p-2) or (j!=q+1 and j!=q-1)) and ((i!=p+1 and i!=p-1) or (j!=q+2 and j!=q-2)):
            table[i][j]=table[i][j-1]+table[i-1][j]
print(table[n][m])
