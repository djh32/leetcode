#coding =utf-8
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [float("-inf")] * (len(nums)+1)
        res = float('-inf')
        for i in range(1,len(nums)+1):
            dp[i] = max(nums[i-1],nums[i-1]+dp[i-1])
            res = max(res,dp[i])
        print(dp)
        return res

# 还有分治方法去解决 强化
Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])