n=int(input())
s=[]
s.append(input().split())
s.append([])
for i in range(0,n):
    s[1].append(10**len(s[0][i]))
for i in range(0,n):
    for j in range(0,i):
        if int(s[0][i])*s[1][j]+int(s[0][j])<int(s[0][j])*s[1][i]+int(s[0][i]):
            s[0][i],s[0][j]=s[0][j],s[0][i]
            s[1][i],s[1][j]=s[1][j],s[1][i]
answer=''
for i in range(n-1,-1,-1):
    answer+=s[0][i]
print(answer)
