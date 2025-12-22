s=input()
if s.isdigit():
    dic=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    s=int(s)
    num= {1000:0,900:0,500:0,400:0,100:0,90:0,50:0,40:0,10:0,9:0,5:0,4:0,1:0}
    for i in num.keys():
        num[i]+=s//i
        s%=i
    i=12
    ans=''
    for j in num.keys():
        ans+=num[j]*dic[i]
        i-=1
    print(ans)
else:
    dic={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    n=0
    i=0
    while i<len(s):
        if i==len(s)-1:
            n+=dic[s[i]]
            i+=1
        else:
            if dic[s[i]]<dic[s[i+1]]:
                n+=dic[s[i+1]]-dic[s[i]]
                i+=2
            else:
                n+=dic[s[i]]
                i+=1
    print(n)