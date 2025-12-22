import sys
column=sys.stdin.readline().split()
n=int(column[0])
column.remove(column[0])
def movef(f,t,m):
    if m==1:
        print(f'1:{column[f]}->{column[t]}')
        return
    else:
        movef(f,3-f-t,m-1)
        print(f'{m}:{column[f]}->{column[t]}')
        movef(3-f-t,t,m-1)
        return
movef(0,2,n)