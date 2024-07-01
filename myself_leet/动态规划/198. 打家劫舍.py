# coding=utf-8
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp = [0, 0] + dp

        for i in range(2, length+2):
            dp[i] = max(dp[i - 2] + nums[i-2], dp[i - 1])
        return max(dp[-1], dp[-2])
print(Solution().rob([2,1,1,2]))




