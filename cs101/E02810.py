import math
n=int(input())
a=[]
for i in range(0,n):
    a.append((i+1)**3)
for i in range(5,n):
    for j in range(1,math.floor((a[i]/3)**(1/3))):
        for k in range(j,math.floor(((a[i]-a[j])/2)**(1/3))):
            if a[i]-a[j]-a[k] in a:
                l=math.ceil((a[i]-a[j]-a[k])**(1/3))
                print('Cube = '+str(i+1)+', Triple = ('+str(j+1)+','+str(k+1)+','+str(l)+')')
