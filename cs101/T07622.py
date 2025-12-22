import sys
n=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
ans=0
def dichotomisef(l,r):
    global data
    global ans
    if r-l==1:
        return
    else:
        mid=int((l+r)/2)
        dichotomisef(l,mid)
        dichotomisef(mid,r)
        l1=l
        r1=mid
        tem=[]
        while True:
            if data[r1]<data[l1]:
                tem.append(data[r1])
                ans+=mid-l1
                if r1==r-1:
                    tem.extend(data[l1:mid])
                    break
                r1+=1
            else:
                tem.append(data[l1])
                if l1==mid-1:
                    tem.extend(data[r1:r])
                    break
                l1+=1
        data[l:r]=tem
dichotomisef(0,n)
print(ans)
