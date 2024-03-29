# coding=utf-8
from typing import List

def lower_bound(nums:List, target)->int:
    # 有序数组中第一个>= target的位置
    # 反正优先记住  len(nums)-1 和l<=r 捆绑 都闭[left, right]
    # 反正优先记住  len(nums) 和l<r 捆绑 左闭右开 [left, right)

    l,r = 0,len(nums)-1
    while l<=r:
        mid = l + (r-l)//2
        if nums[mid] < target:
            l = mid +1
        else:
            r = mid-1
    return l

def lower_bound2(nums:List, target)->int:
    l,r = 0,len(nums) # 左闭右开 [left, right)
    while l<r: # 结束时l=r
        mid = l + (r-l)//2
        if nums[mid] < target:
            l = mid +1
        else:
            r = mid
    return l

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound(nums,target)
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        end = lower_bound(nums,target+1)-1
        return [start,end]

print(Solution().searchRange([1,2,3,5,7,7,8,9,12],7))
#print(lower_bound([1,2,3,5,7,9,12],6))


