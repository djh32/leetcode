from typing import List
import random

'''
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
'''


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_sort(nums, lidx, ridx):  # quick sort 按照左pivot
            rand_idx = random.randint(lidx, ridx)
            nums[lidx], nums[rand_idx] = nums[rand_idx], nums[lidx]
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

        def quick_sort_2(nums, lidx, ridx):  # quick sort 按照左 第一个index 做pivot 都正确
            pivot = lidx
            while lidx < ridx:
                while lidx < ridx and nums[ridx] >= nums[pivot]:
                    ridx -= 1
                while lidx < ridx and nums[lidx] <= nums[pivot]:
                    lidx += 1
                nums[lidx], nums[ridx] = nums[ridx], nums[lidx]
            nums[lidx], nums[pivot] = nums[pivot], nums[lidx]
            return lidx, nums[lidx]
        def quick_sort_3(nums, lidx, ridx):  # 尽量让pivot的index在中间的解法，过滤大量左边重复是1的情况
            partition = nums[lidx]
            l = lidx + 1
            r = ridx
            while True:
                while l <= r and nums[l] <= partition: l += 1
                while r >= l and nums[r] >= partition: r -= 1
                if l >= r: break
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            pivot_idx = min(l, r)  # l,r较小者才是pivot的应该存在的位置。
            nums[pivot_idx], nums[lidx] = nums[lidx], nums[pivot_idx]
            return pivot_idx,nums[pivot_idx]

        # random.shuffle(nums)
        find_now, _ = quick_sort(nums, 0, len(nums) - 1)
        l = len(nums)
        left, right = 0, l - 1
        need = l - k
        while find_now != need:
            if find_now < need:
                while find_now < need and find_now + 1 < need and nums[find_now + 1] == nums[find_now]:
                    find_now += 1
                left = find_now + 1
                find_now, _ = quick_sort(nums, left, right)
            else:
                while find_now > need and find_now - 1 > need and nums[find_now - 1] == nums[find_now]:
                    find_now -= 1
                right = find_now - 1
                find_now, _ = quick_sort(nums, left, right)
        return nums[find_now]

 # quick sort https://blog.csdn.net/qq_69369227/article/details/130040525
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

#print(Solution().findKthLargest(nums, 9))
x = Solution().findKthLargest_2(nums, 2)
#x  = quick_sort_3(nums,0,len(nums)-1)
print(x)
