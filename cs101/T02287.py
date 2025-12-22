import sys
n=int(sys.stdin.readline())
while n!=0:
    t=list(map(int,sys.stdin.readline().split()))
    k=list(map(int,sys.stdin.readline().split()))
    t.sort()
    k.sort()
    ans=0
    t_end=n-1
    k_end=n-1
    t_start=0
    k_start=0
    while t_start<=t_end:
        if t[t_end]>k[k_end]:
            ans+=1
            t_end-=1
            k_end-=1
        elif t[t_end]<k[k_end]:
            ans-=1
            t_start+=1
            k_end-=1
        elif t[t_start]>k[k_start]:
            ans+=1
            t_start+=1
            k_start+=1
        elif t[t_start]==k[k_start]:
            if t[t_end]==t[t_start]:
                break
            else:
                ans-=1
                t_start+=1
                k_end-=1
        else:
            t_start+=1
            k_end-=1
            ans-=1
    print(ans*200)
    n=int(sys.stdin.readline())