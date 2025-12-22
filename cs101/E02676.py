k=int(input())
a=input().split()
for i in range(0,k):
    a[i]=int(a[i])
a_1=0
a_2=0
a_3=0
for i in a:
    if i==1:
        a_1+=1
    if i==5:
        a_2+=1
    if i==10:
        a_3+=1
print(a_1)
print(a_2)
print(a_3)
