class Solution:
    def rob(self, nums: List[int]) -> int:
        import copy
        dp=copy.deepcopy(nums)
        for i in range(2,len(nums)):
            for j in range(i-1):
                dp[i]=max(dp[i],dp[j]+nums[i])
        dp.sort()
        return dp[-1]