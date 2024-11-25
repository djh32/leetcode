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
    def lengthOfLISDF(self, nums: List[int]) -> int:
        dp = [1 for  _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        #print(dp)
        return max(dp[-1])

    def lengthOfLIS_binserch(self, nums: List[int]) -> int:
        holder = [nums[0]]
        for i in range(len(nums)):
            if nums[i]>holder[-1]:
                holder.append(nums[i])
            else:
                insert_idx =self.bin_search_left(holder,nums[i])
                holder[insert_idx] = nums[i]
        return len(holder)

    def bin_search_left(self,st_nums,find):
        #l,r = 0,len(st_nums)
        #while l<r:
        l, r = 0, len(st_nums) - 1
        while l<=r:
            mid = (l+r)//2
            if st_nums[mid] == find:
                r = mid-1
            elif st_nums[mid] < find:
                l = mid+1
            else:
                r=mid-1
        return l


print(Solution().lengthOfLIS_binserch([1,3,14,6,8,2,7,9]))

