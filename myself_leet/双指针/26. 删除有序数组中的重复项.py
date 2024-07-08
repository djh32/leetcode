# coding=utf-8
from typing import List

"""
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
        return a+1, nums # a是index 整体数量是a+1


print(Solution().removeDuplicates([1,1,2]))
