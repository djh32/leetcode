# coding=utf-8

from typing import List, Optional

"""
给你一个数组，让你进行归并排序
"""


def quick_sort(nums):
    l, r = 0, len(nums) - 1
    pivot = nums[l]
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    return l, nums


def dfs(nums):
    if len(nums) == 0:
        return nums
    mid, nums = quick_sort(nums)
    left = dfs(nums[:mid])
    mids = [nums[mid]]
    right = dfs(nums[mid + 1:])
    return left + mids + right
s = [-7,2,-2,-2,1,4,5]
print(dfs(s))

