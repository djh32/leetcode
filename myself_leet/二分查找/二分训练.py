from typing import List
import random

'''
二分算法的训练，寻找左边右边边界的训练
'''
import random


def bin_to_left_find(nums: List[int], target) -> int:
    print(nums,target)
    l, r = 0, len(nums) - 1  # []
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            r = mid-1
        elif nums[mid] < target:
            l = mid +1
        else:
            r = mid - 1
    print(l)
    return r

def bin_to_left_find_sec(nums: List[int], target) -> int:
    print(nums,target)
    l, r = 0, len(nums)  # [)
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            r = mid
        elif nums[mid] < target:
            l = mid +1
        else:
            r = mid
    print(l)
    return r

def bin_to_right_find_sec(nums: List[int], target) -> int:
    print(nums,target)
    l, r = 0, len(nums)  # [)
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            l = mid+1
        elif nums[mid] < target:
            l = mid +1
        else:
            r = mid
    print(l,r) #same r,l
    return r-1

def bin_to_right_find(nums: List[int], target) -> int:
    print(nums,target)
    l, r = 0, len(nums)-1  # []
    while l <= r: # l= r+1
        mid = l + (r-l)//2
        if nums[mid] == target:
            l = mid+1
        elif nums[mid] < target:
            l = mid +1
        else:
            r = mid -1
    print(l,r) #same r,l
    return r

array = [random.randint(1, 10) for _ in range(10)]
bin_to_right_find(sorted(array),6)
