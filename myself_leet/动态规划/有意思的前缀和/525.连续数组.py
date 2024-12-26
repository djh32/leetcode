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
class Solution2: # Error 没有max
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


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = {0:-1} # 需要哨兵保证[0,1],[1,0] 结果正确
        sums = 0
        res = 0
        for i in range(len(nums)):
            sums += 1 if nums[i] == 1 else -1
            if sums not in cache:
                cache[sums] = i
            else:
                res = max(i - cache[sums],res)
            # cache[sums]是上一个 前缀和 的位置，
            # 如果上一个前缀和出现，代表中间被减小再增加了，或者增加再减小了，
            # 出现就代表有相加等于0的结果需要比较。
            # if sums ==0:
            #     res = max(i+1,res)
        return res
sol = Solution().findMaxLength([1,1,0,0,1,1])
print(sol)
