import sys
pascal=list(sys.stdin.readline())
pascal=pascal[:-1]
a=b=c=0
l=len(pascal)
i=0
while i<l:
    if pascal[i]=='a':
        i+=3
        a=int(pascal[i])
        i+=2
    elif pascal[i]=='b':
        i+=3
        b=int(pascal[i])
        i+=2
    elif pascal[i]=='c':
        i+=3
        c=int(pascal[i])
        i+=2
print(a,b,c)