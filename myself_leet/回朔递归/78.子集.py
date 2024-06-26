# coding=utf-8
from typing import List

"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的
子集
（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cache:list, left_nums):
            if not left_nums:
                return

            for i in range(len(left_nums)):
                cache.append(left_nums[i])
                left = left_nums[i+1:]
                res.append(cache.copy())
                dfs(cache,left)
                cache.pop()
        dfs([],nums)
        res.append([])
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int) -> None:
            if i == n:  # 子集构造完毕
                ans.append(path.copy())  # 复制 path，也可以写 path[:]
                return

            # 选 nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()  # 恢复现场

            # 不选 nums[i]
            dfs(i + 1)



        dfs(0)
        return ans

print(Solution().subsets([1,2,3]))
