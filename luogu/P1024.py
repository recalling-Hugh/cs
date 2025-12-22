x=input().split()
t=0.000001
p=[]
ans=[]
a=''
for i in range(0,4):
    x[i]=float(x[i])
def calculatef(n):
    return x[0]*n**3+x[1]*n**2+x[2]*n+x[3]
def dichotomizef(l,r):
    if -t<calculatef((l+r)/2)<t:
        return((l+r)/2)
    if calculatef((l+r)/2)>=t:
        if calculatef(l)<=-t:
            return dichotomizef(l,(l+r)/2)
        else:
            return dichotomizef((l+r)/2,r)
    else:
        if calculatef(l)>=-t:
            return dichotomizef(l,(l+r)/2)
        else:
            return dichotomizef((l+r)/2,r)
for i in range(-100,100):
    if -t<calculatef(i)<t:
        ans.append(i)
        continue
    if -t<calculatef(i+1)<t:
        continue
    if calculatef(i)*calculatef(i+1)<0:
        ans.append(dichotomizef(i,i+1))
for i in ans:
    p.append(round(i,2))
print(f'{p[0]:.2f}'+' '+f'{p[1]:.2f}'+' 'f'{p[2]:.2f}')
