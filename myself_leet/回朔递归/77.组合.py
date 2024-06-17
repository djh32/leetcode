#coding=utf-8
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1,n+1)
        res = []

        def dfs(nums,path:List,begin,k):
            if len(path) == k:
                res.append(path.copy())

            for i in range(begin,len(nums)):
                path.append(nums[i])
                dfs(nums,path,i + 1 ,k)
                path.pop(-1)

        dfs(nums,[],0,k)
        return res
print(Solution().combine(n=4,k=2))






