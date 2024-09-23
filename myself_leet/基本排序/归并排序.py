# coding=utf-8

from typing import List, Optional

"""
给你一个数组，让你进行归并排序
"""


class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:
        nums = self.dfs(nums)
        return nums

    def sub_merge(self, nums1, nums2):
        i, j = 0, 0
        ret_temp_list = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                ret_temp_list.append(nums1[i])
                i += 1
            else:
                ret_temp_list.append(nums2[j])
                j += 1
        if i < len(nums1):
            ret_temp_list.extend(nums1[i:])
        elif j < len(nums2):
            ret_temp_list.extend(nums2[j:])
        return ret_temp_list

    def dfs(self, nums):
        if len(nums) == 1:
            return nums
        m = len(nums) // 2
        left = self.dfs(nums[:m])
        right = self.dfs(nums[m:])
        tmp = self.sub_merge(left, right)
        return tmp


print(Solution().mergeSort([8, 4, 5, 7, 1, 3, 6, 2]))
