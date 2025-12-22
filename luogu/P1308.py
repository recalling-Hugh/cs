w=input()
s=input()
a=' '
word=''
ans=[]
num=0
l=len(w)
for i in w:
    if 65<=ord(i)<=90:
        word+=chr(ord(i)+32)
    else:
        word+=i
for i in range(0,len(s)):
    if 65<=ord(s[i])<=90:
        a+=chr(ord(s[i])+32)
    else:
        a+=s[i]
        if i>=l:
            if a[i+1]==word[-1]:
                if a[i-l+2:i+2]==word and a[i-l]==' ' and(s[i+1]==' ' or i==len(s)-1):
                    num+=1
                    ans.append(i-l+1)
if num!=0:
    w=str(num)+' '+str(ans[0])
    print(w)
else:
    print('-1')
