#cdoing=utf-8
from typing import List

def heapify(nums: List[int]) -> List[int]:
    size = len(nums)

    for idx in range(size//2)[::-1]:
        sift_down_iter(nums,idx,size)
    return nums

def sift_down_iter(nums:List[int],idx: int,size: int) -> None: # 大根堆变换
    if idx * 2 + 1 > size:
        return

    left,right = idx*2+1,idx*2+2
    large_child_idx = left
    if right<size and nums[large_child_idx]<nums[right]:
        large_child_idx = right

    if nums[large_child_idx]>nums[idx]:
        nums[idx],nums[large_child_idx] = nums[large_child_idx],nums[idx]

    sift_down_iter(nums,large_child_idx,size)



print(heapify([1,2,5,6,2,1,4,1,2,7,8,9,10]))



