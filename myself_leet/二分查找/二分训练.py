from typing import List
import random

'''
二分算法的训练，寻找左边右边边界的训练
'''
import random


def bin_to_left_find(nums: List[int], target) -> int:
    print(nums, target)
    # 使用【】的时候要考虑边界，
    # 收缩右侧边界，向左收敛的话，需要考虑出界情况，left >= nums.length
    l, r = 0, len(nums) - 1  # []
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print(l)
    return l


def bin_to_left_find_sec(nums: List[int], target) -> int:
    # 收缩右侧边界，向左收敛的话，需要考虑出界情况，结果会 l=r >len(nums) 但是左侧肯定从0开始
    print(nums, target)
    l, r = 0, len(nums)  # [)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            r = mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    print(l)
    return r


def bin_to_right_find_sec(nums: List[int], target) -> int:
    # 收缩左侧边界，向右收敛的话，需要考虑出界情况，结果会 l=r <=0 但是右侧肯定从len-1开始
    # bisect.bisect_right
    print(nums, target)
    l, r = 0, len(nums)  # [)
    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    print(l, r)  # same r,l
    return r - 1


def bin_to_right_find(nums: List[int], target) -> int:
    # 使用【】的时候要考虑边界，
    # 收缩左侧边界，向右收敛的话，需要考虑出界情况，right <=0
    # bisect.bisect_right
    print(nums, target)
    l, r = 0, len(nums) - 1  # []
    while l <= r:  # l= r+1
        mid = l + (r - l) // 2
        if nums[mid] == target:
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print(l, r)  # same r,l
    return r


array = [random.randint(1, 10) for _ in range(10)]
print(bin_to_right_find_sec([1, 6, 6, 6, 6, 10], 0))
import bisect

print(bisect.bisect_right([1, 6, 6, 6, 6, 10], 0) - 1)
