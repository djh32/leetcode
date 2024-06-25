from typing import List
"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        def dfs(nums,path:List):
            if len(path) == size:
                result.append(path.copy())
                return
            for index in range(len(nums)):
                pick = nums[index]
                left = nums[:index] + nums[index+1:]
                path.append(pick)
                dfs(left,path)
                path.pop(-1)
        dfs(nums,[])
        return result
print(Solution().permuteUnique([1,2,3]))