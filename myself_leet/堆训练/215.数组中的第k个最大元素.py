from typing import List
import random

'''
输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
'''


class Solution:
    def findKthLargestHeapq(self, nums: List[int], k: int) -> int:
        import heapq
        res = []
        need_heap_size = len(nums) - k + 1  # 大根堆, 因此需要保留len - k + 1个元素,堆顶即是topk大.

        for i in range(len(nums)):
            heapq.heappush(res, -nums[i])
            if len(res) > need_heap_size:
                heapq.heappop(res)
        return -res[0]


nums = [3, 2, 1, 4, 5, 1, 1, 1, 1, 1, 1, 1]
# print(quick_sort(nums, 0, len(nums) - 1))

# print(Solution().findKthLargest(nums, 5))
print(Solution().findKthLargestHeapq(nums, 8))
