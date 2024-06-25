from typing import List


class TestJob:
    def merge_two_nums(self, nums1: List[int], m, nums2: List[int], n):
        pos_end = m + n - 1
        while pos_end >= 0 and m - 1 >= 0 and n - 1 >= 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[pos_end] = nums1[m - 1]
                m -= 1
            else:
                nums1[pos_end] = nums2[n - 1]
                n -= 1
            pos_end -= 1
        while n - 1 >= 0:
            nums1[pos_end] = nums2[n - 1]
            n -= 1
            pos_end -= 1
        return nums1


n1 = [3, 4, 8]
n2 = [8, 14]
m = len(n1)
n1 = n1 + [0 for i in range(len(n2))]
n = len(n2)

print(TestJob().merge_two_nums(n1, m, n2, n))


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


s = [-7,2,-2,-2,1,4,5]
# s = [5,6]
s = dfs(s)
print(s)
