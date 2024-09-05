from typing import List
from copy import deepcopy

"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。
注意：解集不能包含重复的组合。 

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(path, candidates, begin):
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(deepcopy(path))
                return

            for i in range(begin, len(candidates)):

                if sum(path) > target: break  # 提前结束不进行搜索遍历

                if i > begin and candidates[i] == candidates[i - 1]:
                    continue  # 这个真牛逼，这i>begin的意思是本轮已经找过一次数据，并且连续 [1,2,2,2,4] i=2的时候不寻找。

                path.append(candidates[i])
                dfs(path, candidates, i + 1)
                path.pop(-1)

        dfs([], sorted(candidates), 0)
        return res


print(Solution().combinationSum2([2, 5, 2, 1, 2,2,2,2,2,2,2], target=5))
