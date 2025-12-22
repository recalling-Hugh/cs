import sys
n=int(sys.stdin.readline())
def multf(a,b,mod=32767):
    return [
        [(a[0][0]*b[0][0]+a[0][1]*b[1][0])%mod,
         (a[0][0]*b[0][1]+a[0][1]*b[1][1])%mod],
        [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%mod,
         (a[1][0]*b[0][1]+a[1][1]*b[1][1])%mod]
    ]
def powf(base,power,mod=32767):
    result=[[1,0],[0,1]]
    while power>0:
        if power&1:
            result=multf(result,base,mod)
        base=multf(base,base,mod)
        power>>=1
    return result
for i in range(n):
    data=int(sys.stdin.readline())
    if data==1:
        print(1)
    elif data==2:
        print(2)
    else:
        ans=powf([[2,1],[1,0]],data-2,mod=32767)
        print((ans[0][0]*2+ans[0][1]*1)%32767)