# coding=utf-8
from typing import List

"""
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。


示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释:结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hold_min, hold_max = nums[0], nums[0]
        res = hold_max
        for i in range(1, len(nums)):
            # hold_max,hold_min互相不能影响,所以用一个式子表达
            hold_min, hold_max = min(nums[i], nums[i] * hold_max, nums[i] * hold_min), max(nums[i], nums[i] * hold_max,
                                                                                           nums[i] * hold_min)
            res = max(res, hold_max)
        return res


print(Solution().maxProduct([-2]))
