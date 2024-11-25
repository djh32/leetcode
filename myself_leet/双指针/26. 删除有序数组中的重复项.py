# coding=utf-8
from typing import List

"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。


[0,0,0,1,1,2,3,3,3,4,5,6]
输出[0,1,2,3,4,5,6] res = 7
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a, b = 0, 0
        lens = len(nums)
        while b < lens:
            while b < lens and nums[a] == nums[b] :
                b += 1
            if b >= lens: break
            a += 1
            nums[a] = nums[b]
        return a+1, nums[:a+1] # a是index 整体数量是a+1


print(Solution().removeDuplicates([0,0,0,1,1,2,3,3,3,4,5,6]))
