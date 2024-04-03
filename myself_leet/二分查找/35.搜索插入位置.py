from typing import List
class Solution:

    def searchInsert2(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # [left,right]
        while l <= r:  # 结束 l会比r多一个结束 l是结束位置
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return l

    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1  # [left,right]
        while l <= r:  # 结束 l会比r多一个结束 l是结束
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] >= target: # 这里必须>=才行 如果只是> 会死循环  所以必须使用else或者>=
                r = m - 1
        return l
print(Solution().searchInsert([1,3,5,6],5))