# coding=utf-8
from typing import List


# -1 -1 0 1 2
def three_sums(nums: List[int]):
    st_nums = sorted(nums, key=lambda a: a)
    res = []
    for i in range(len(st_nums)-2):
        if st_nums[i] > 0: break  # r > l > i > 0
        if i > 0 and st_nums[i - 1] == st_nums[i]: continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sums = st_nums[i] + st_nums[r] + st_nums[l]
            if sums > 0:
                r -= 1
            elif sums < 0:
                l += 1
            else:
                res.append([st_nums[i], st_nums[r], st_nums[l]])
                while l<r and st_nums[l]==st_nums[l +1]:
                    l +=1
                while l<r and st_nums[r]==st_nums[r-1]:
                    r -=1
                l +=1
                r -=1
    return res

print(three_sums([-1,-1,2,3,1,4,2,2,1,3,4,-2,-3,-4,5,1,0,0]))
