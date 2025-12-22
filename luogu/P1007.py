l=int(input())
n=int(input())
if n==0:
    print('0 0')
else:
    least=0
    most=0
    c=input().split()
    for i in range(0,n):
        s=int(c[i])
        if s<=l/2:
            least=max(least,s)
            most=max(most,l+1-s)
        else:
            least=max(least,l+1-s)
            most=max(most,s)
    print(str(least)+' '+str(most))
