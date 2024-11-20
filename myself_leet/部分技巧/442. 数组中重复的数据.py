import sys
from typing import List, Optional

"""
442. 数组中重复的数据
中等
相关标签
相关企业
给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 最多两次 。请你找出所有出现 两次 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间（不包括存储输出所需的空间）的算法解决此问题。
"""


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        res = []
        while i < len(nums):
            tmp = nums[i]
            if tmp - 1 == i or tmp < 0:
                i += 1
                continue
            if tmp == nums[tmp - 1]:
                res.append(tmp)
                nums[i] *= -1
            else:
                nums[tmp - 1], nums[i] = nums[i],nums[tmp - 1]
                i -= 1
            i += 1
        return res


print(Solution().findDuplicates([1, 1]))
