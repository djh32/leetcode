from typing import List


class Solution:
    def quick_sort(self, nums, l, r):
        pivot = nums[l]
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l]= pivot
        return l

    def find_max_k_sublist(self, nums: List[int], k:int):
        #need_idx = len(nums)-k # 后k个大的
        need_idx = k  # 前k个小的

        find_now = self.quick_sort(nums, 0, len(nums) - 1)
        while find_now != need_idx:
            if find_now < need_idx:
                find_now = self.quick_sort(nums,find_now+1,len(nums)-1)
            elif find_now > need_idx:
                find_now = self.quick_sort(nums, 0, find_now)
        #return nums[find_now:]# 后k个大的
        return nums[:need_idx]# 前k个小的




print(Solution().find_max_k_sublist([25,30,35,10,5,15,20,40],6))
