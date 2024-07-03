from typing import List

"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

 

示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = {}
        sums = 0
        res = 0
        for i in range(len(nums)):
            sums += 1 if nums[i] == 1 else -1
            if sums not in cache:
                cache[sums] = i
            else:
                res = i - cache[sums]
            if sums ==0:
                res = i+1
        return res

sol = Solution().findMaxLength([0,1,1,0,1,1,1,0]

)
print(sol)
