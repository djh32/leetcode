# coding=utf-8
from typing import List
"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,zero) = 0
        # [zero,i) = 1
        # [i,two) = 2
        zero = i = 0
        two = len(nums) - 1
        while i <= two:
            i_color = nums[i]
            if i_color == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            elif i_color == 1:
                i += 1
            else:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1

x = [2,0,1]
Solution().sortColors(x)
print(x)
