class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import copy
        def searchf(a,l,t):
            added=copy.deepcopy(a)
            left=copy.deepcopy(l)
            if len(left)==1:
                added.extend(left)
                t.append(added)
            else:
                left_1=copy.deepcopy(left)
                for i in left_1:
                    added.append(i)
                    left.remove(i)
                    t=searchf(added,left,t)
                    added.remove(i)
                    left.append(i)
            return t
        ans=searchf([],nums,[])
        return ans