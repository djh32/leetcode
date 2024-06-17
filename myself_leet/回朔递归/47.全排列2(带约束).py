from typing import List
"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)
        def dfs(nums,path:List):
            if len(path) == size:
                result.append(path.copy())
                return
            layer_have_seen_item = []
            for index in range(len(nums)):
                if nums[index] in layer_have_seen_item:
                    continue
                pick = nums[index]
                left = nums[:index] + nums[index+1:]
                path.append(pick)
                dfs(left,path)
                path.pop(-1)
                layer_have_seen_item.append(pick)

        dfs(nums,[])
        return result
print(Solution().permuteUnique([1,2,3]))