# coding=utf-8
from typing import List
# [0,1,2,3,4,5]

import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        for ind in range(len(nums)):
            while q and nums[q[-1]] <= nums[ind]: q.pop()  # 保证序列降序的逻辑，非降序就删除。
            while q and ind - q[0] >= k: q.popleft()  # 序列满了，在添加>k个了。因此需要腾出一个位置给新的append
            q.append(ind)
            if ind >= k - 1:  # 这里是窗口已经形成的时候了，可以往结果里面添加了的意思
                res.append(nums[q[0]])
        return res


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:  # 当前序列满了，在添加>k个了。因此需要腾出一个位置给新的append
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

# 作者：Krahets
# 链接：https://leetcode.cn/problems/sliding-window-maximum/solutions/2361228/239-hua-dong-chuang-kou-zui-da-zhi-dan-d-u6h0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
