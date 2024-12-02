#coding=utf-8
"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：

输入：nums = [1,3,4,2,2]
输出：2
示例 2：

输入：nums = [3,1,3,4,2]
输出：3
示例 3 :

输入：nums = [3,3,3,3,3]
输出：3

"""
from typing import List

class Solution:
    def findDuplicateError(self, nums: List[int]) -> int:  # 错误的搞笑解法，只能重复一次，不能重复多次。 [2,5,9,6,9,3,8,9,7,1] 失败
        slowIdx,fastIdx = 0,0
        first = True
        while nums[fastIdx] != nums[slowIdx] or slowIdx == fastIdx or first:
            slowIdx = nums[slowIdx]
            fastIdx = nums[nums[fastIdx]]
            first = False
        return nums[fastIdx]
    """
    low = fast 时，快慢指针相遇，low 走过的距离是初始点（0）到环状开始的点 （x） 加上 环状开始的点（x） 到相遇点（y） 这段距离，
    而fast走过的距离是 初始点（0）到环状开始的点（x），点（x） 到点（y），点（y）到点（x），点（x）到点（y）。
    又因为fast走过的距离是low的两倍，设0到x长度为a，x到y长度为b,则有2*（a+b） = a+ b+ (y到x的距离) + b，则y到x的距离就等于0到x的距离。所以当新的两个指针 一个从0出发，一个从相遇点y出发时，他们走到的相同的值就是环状开始的点，即x点。
    """

    def findDuplicate(self, nums: List[int]) -> int:
        slowIdx,fastIdx = 0,nums[0]
        while slowIdx!=fastIdx: # 首先找到环中的命中点
            slowIdx = nums[slowIdx]
            fastIdx = nums[nums[fastIdx]]

        p1,p2 = 0,nums[slowIdx]
        # 这个地方注意， 0是起始点没有意义， slow = fast 是快慢的命中点，不是环的起始点，找环的起始点需要走从0到命中步即可。
        while nums[p1] != nums[p2]:
            p1 = nums[p1]
            p2 = nums[p2]
        return nums[p1]


print(Solution().findDuplicate([2,5,9,6,9,3,8,9,7,1]))




