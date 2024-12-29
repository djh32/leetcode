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

    def maxSubArrayFindIdx(self, nums: List[int]) -> int:
        dp_last = nums[0]
        # dp = max(dp_last+nums[i], nums[i]) =>
        # if dp_last<0 then nums[i]
        # else dp_last + nums[i]
        begin = 0
        max_dp = nums[0] # 这里必须是nums【0】 因为 [-1,-2] 从idx=1开始，如果是-inf的话缺失对比-1的而忽略了。
        res = [0,0]
        for i in range(1,len(nums)):
            if dp_last<0:
                dp_last = nums[i]
                begin = i
            else:
                dp_last += nums[i]
            dp_now_check = dp_last
            if dp_now_check > max_dp:
                max_dp = max(max_dp,dp_now_check)
                res[0] = begin
                res[1] = i
        return sum(nums[res[0]:res[1]+1])




# 还有分治方法去解决 强化
#print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArrayFindIdx([-2,1,-3,4,-1,2,1,-5,4]))
