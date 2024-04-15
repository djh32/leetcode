#coding=utf-8
from typing import List
#[0,1,2,3,4,5]

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        for ind in range(len(nums)):
            while q and nums[q[-1]] <= nums[ind]:q.pop()
            while q and ind - q[0] >=k :q.popleft()
            q.append(ind)
            if ind >= k -1 : # 这道题的顺序很重要 当ind当前的数据至少看了k次才能添加结果。不能操作数据，操作index索引会好考虑
                res.append(nums[q[0]])
        return res







