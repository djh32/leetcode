from typing import List
import random

'''
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, lidx, ridx):
            pivot = random.randint(lidx, ridx)
            cache = nums[pivot]
            while lidx < ridx:
                while lidx < ridx and nums[lidx] <= nums[pivot]:
                    lidx += 1
                nums[lidx] = nums[ridx]
                while lidx < ridx and nums[ridx] >= nums[pivot]:
                    ridx -= 1
                nums[ridx] = nums[lidx]


def quick_sort(nums, lidx, ridx):
    pivot = 0
    cache = nums[pivot]
    while lidx < ridx:
        while lidx < ridx and nums[ridx] >= cache:
            ridx -= 1
        nums[lidx] = nums[ridx]
        while lidx < ridx and nums[lidx] <= cache:
            lidx += 1
        nums[ridx] = nums[lidx]
    nums[ridx] = cache
    return nums


nums = [3,1,1,1,1, 2]
print(quick_sort(nums, 0, len(nums) - 1))
