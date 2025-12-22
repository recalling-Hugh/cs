n=int(input())
month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for i in range(0,n):
    data=list(map(int,input().split()))
    p=0
    if data[0]==data[3]:
        p=data[4]-data[1]
    else:
        for j in range(data[0]+1,data[3]):
            p+=month[j]
        p+=month[data[0]]-data[1]+data[4]
    print(data[2]*2**p)
