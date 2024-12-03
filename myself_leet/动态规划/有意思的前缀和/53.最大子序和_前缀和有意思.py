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
    # 前缀和
    # 来自：
    # https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/solutions/2377930/liang-chong-fang-fa-dong-tai-gui-hua-qia-dczr/
    def maxSubArrayPreSum(self, nums: List[int]) -> int:
        min_sum = 0
        s = 0
        result = float('-inf')
        #result = nums[0]
        for n in nums:
            s += n
            result = max(s-min_sum,result) # 23 24行不能交换，用当前s 和 之前min_sum比较，才能找到正确的结果。不能先更新min_sum，否则过不了单长度[-1]
            min_sum = min(min_sum, s)
        return result


# 还有分治方法去解决 强化
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArrayPreSum([-2]))
