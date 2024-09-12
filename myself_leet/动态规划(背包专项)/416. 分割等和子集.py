# coding=utf-8
from typing import List

"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集


"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # # 必须偶数个nums否则false 自己写错了
        # if len(nums) % 2 != 0:
        #     return False

        # sum必须是偶数，否则不符合条件
        if sum(nums) % 2 != 0:return False

        tars = sum(nums) // 2
        row, col = len(nums), tars

        table = [[False for _ in range(col + 1)] for _ in range(row + 1)]  # 这里0column是很重要的，j=0的时候，都为True，0是能到0的

        for i in range(1, row + 1):
            for j in range(col + 1):
                if j == 0:
                    table[i][j] = True  # j=0的时候，都为True，0是能到0的
                else:
                    # 需要使用nums[i-1] 因为i从1开始，遍历逻辑需要判断num0-n所以是i-1
                    find_idx = j - nums[i-1]  # 当前的j是sum[i][j]能否到达j的标记 ,j<=nums[i]的时候需要判断是否能通过组合
                    if find_idx >= 0:
                        table[i][j] = table[i - 1][j - nums[i-1]] or table[i - 1][j]
                    else:
                        table[i][j] = table[i - 1][j]
        print(table)
        return table[-1][-1]
print(Solution().canPartition([3,3,3,4,5]))



