#coding=utf-8
'''
1493. 删掉一个元素以后全为 1 的最长子数组

给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。

提示 1：

输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
示例 2：

输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
示例 3：

输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。

'''

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last_zero_idx = -1
        wind_l, wind_r = 0, 0
        max_len = float("-inf")
        for idx in range(len(nums)):
            wind_r = idx
            if nums[idx] == 0:
                wind_l = last_zero_idx + 1
                last_zero_idx = idx

            max_len = max(max_len, wind_r - wind_l)
        return max_len



print(Solution().longestSubarray([1,0]))



