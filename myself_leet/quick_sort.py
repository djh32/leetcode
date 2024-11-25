from typing import List


class Solution:
    def quick_sort(self, nums: List,l,r):
        pivot = nums[0]
        #l, r = 0, len(nums) - 1
        while l < r:
            while l < r and pivot <= nums[r]:
                r -= 1
            nums[l] = nums[r]
            while l < r and pivot >= nums[l]:
                l += 1
            nums[r] = nums[l]
            nums[l] = pivot
        return l

    def dfs_sort(self, nums, l, r):
        if l >=r:
            return
        m = self.quick_sort(nums,l,r)
        self.dfs_sort(nums,l,m-1)
        self.dfs_sort(nums, m+1, r)

    def run_sort(self,nums):
        self.dfs_sort(nums,0,len(nums)-1)
        return nums


print(Solution().run_sort([12, 6, 1, 15, 0, 5, 11, 10]))
