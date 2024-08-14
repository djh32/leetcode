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

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, lidx, ridx):
            pivot = lidx
            cache = nums[pivot]
            while lidx < ridx:
                while lidx < ridx and nums[ridx] >= cache:
                    ridx -= 1
                nums[lidx] = nums[ridx]
                while lidx < ridx and nums[lidx] <= cache:
                    lidx += 1
                nums[ridx] = nums[lidx]
            nums[lidx] = cache
            return lidx, nums[lidx]

        # pivot_idx = random.randint(0, len(nums) - 1)  # 随机选择pivot
        # nums[0], nums[pivot_idx] = nums[pivot_idx], nums[0]  # pivot放置到最左边
        random.shuffle(nums)
        find_now, _ = quick_sort(nums, 0, len(nums) - 1)
        l = len(nums)
        need = l - k
        while find_now != need:
            if find_now < need:
                find_now, _ = quick_sort(nums, find_now + 1, len(nums) - 1)
            else:
                find_now, _ = quick_sort(nums, 0, find_now - 1)
        return nums[find_now]


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


nums = [3,2,1,5,6,4]
# print(quick_sort(nums, 0, len(nums) - 1))

print(Solution().findKthLargest2(nums, 2))
