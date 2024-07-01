# coding=utf-8
from typing import List

"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 
子数组
 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        length = len(nums)
        sums = 0
        left, right = 0, 0
        while right < length:
            sums += nums[right]
            while sums >= target:
                res = min(res, right - left + 1)
                sums -= nums[left]
                left += 1
            right += 1
        return 0 if res == float("inf") else res


print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))
