class Solution:
    def longestPalindrome(self, s: str) -> str:
        string=list(s)
        l=len(string)
        ans=string[0]
        num=1
        for i in range (l):
            j=1
            n=1
            while i>=j and i+j<l:
                if string[i-j]==string[i+j]:
                    n+=2
                    if n>num:
                        num=n
                        ans=(''.join(map(str,string[i-j:i+j+1])))
                    j+=1
                else:
                    break
        for i in range(l-1):
            if string[i]==string[i+1]:
                j=1
                n=2
                if n>num:
                    num=n
                    ans=(''.join(map(str,string[i:i+2])))
                while i>=j and i+j+1<l:
                    if string[i-j]==string[i+j+1]:
                        n+=2
                        if n>num:
                            num=n
                            ans=(''.join(map(str,string[i-j:i+j+2])))
                        j+=1
                    else:
                        break
        return(ans)