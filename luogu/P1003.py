answer=-1
n=int(input())
s=[0]
for i in range(1,n+1):
    s.append(input().split())
l=input().split()
p=int(l[0])
q=int(l[1])
for i in range(1,n+1):
    if p>=int(s[i][0]) and q>=int(s[i][1]) and p<=int(s[i][0])+int(s[i][2]) and q<=int(s[i][1])+int(s[i][3]):
        answer=i
print(answer)
