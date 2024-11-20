from typing import List


class Solution:
    def sort_abs_list(self, nums: List[int]):
        res = [None for _ in range(len(nums))]
        end = len(res) - 1
        l, r = 0, end
        while end >= 0:
            if abs(nums[l]) >= abs(nums[r]):
                res[end] = abs(nums[l])
                l += 1
            else:
                res[end] = abs(nums[r])
                r -= 1
            end -= 1
        return res


x = Solution().sort_abs_list([-17, -12, -6, 12, 16])
print(x)
'''
以下是自己瞎写的代码。带绝对值的快速排序。
'''


def quick_sort(nums):
    l, r = 0, len(nums) - 1
    petric = abs(nums[l])
    while l < r:
        while l < r and abs(nums[r]) >= petric:
            r -= 1
        nums[l] = abs(nums[r])
        while l < r and abs(nums[l]) <= petric:
            l += 1
        nums[r] = abs(nums[l])
    nums[l] = petric
    return l, nums


def dfs(nums):
    if len(nums) == 0:
        return nums
    mid, nums = quick_sort(nums)
    left = dfs(nums[:mid])
    mids = [nums[mid]]
    right = dfs(nums[mid + 1:])
    return left + mids + right


s = [-7, 2, -2, -2, 1, 4, 5]
# s = [5,6]
s = dfs(s)
print(s)
