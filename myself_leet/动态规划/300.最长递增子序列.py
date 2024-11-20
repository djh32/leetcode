# coding=utf-8
from typing import List

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
子序列
。

 
示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
 


"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)时间 + O(n)空间
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)

    def lengthOfLISOnlogn(self, nums: List[int]) -> int:
        # [7,8,9,1,2,3,10,12] 利用有序数组结合二分法，能二分快速找到o(logn)有序数组里面的替换位置，
        holder = [0] * len(nums)
        result_num = 0
        for k in nums:
            left, right = 0, result_num - 1  # [left,right] 所以需要 left<=right
            while left <= right:
                m_idx = (left + right) // 2
                if holder[m_idx] == k:
                    #left = m_idx +1  #允许非连续
                    right = m_idx -1 # 不允许连续
                elif holder[m_idx] > k:
                    right = m_idx - 1
                else:
                    left = m_idx + 1
            holder[left] = k
            if left == result_num:
                result_num += 1
                holder[left] = k
        #print(holder)
        return result_num


# print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(Solution().lengthOfLISOnlogn([7, 8, 9, 1, 2, 3, 10,8,8, 12]))
