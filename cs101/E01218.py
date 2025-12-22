l=int(input())
a=[]
for i in range(0,l):
    a.append(int(input()))
for i in a:
    j=1
    while j**2<=i:
        j+=1
    print(j-1)
