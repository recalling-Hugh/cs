n=int(input())
a=[]
flag=True
dic={'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4','H':'4','I':'4','J':'5','K':'5','L':'5','M':'6','N':'6','O':'6','P':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9','X':'9','Y':'9'}
num=['0','1','2','3','4','5','6','7','8','9']
for i in range(0,n):
    a.append(input())
    a[i]=a[i].replace('-','')
    for j in range(0,7):
        if a[i][j] not in num:
            a[i]=a[i][:j]+dic[a[i][j]]+a[i][j+1:]
    a[i]=a[i][:3]+'-'+a[i][3:]
a.sort()
ans={}
for i in a:
    if i in ans.keys():
        ans[i]+=1
    else:
        ans[i]=1
for i in ans.keys():
    if ans[i]>=2:
        print(i,ans[i])
        flag=False
if flag:
    print('No duplicates.')
