# coding=utf-8
from typing import List


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
