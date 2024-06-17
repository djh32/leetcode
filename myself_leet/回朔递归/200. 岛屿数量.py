# coding=utf-8
from typing import List

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 
"""


class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i >= 0 and j >= 0 and i < row and j < col and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
            else:
                return

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result

    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])

        def bfs(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop(0)
                grid[i][j] = "0"
                for sums in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nxt_i = i + sums[0]
                    nxt_j = j + sums[1]
                    if nxt_i >= 0 and nxt_j >= 0 and nxt_i < row and nxt_j < col and grid[nxt_i][nxt_j] == "1":
                        stack.append([nxt_i, nxt_j])
            return None

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    result += 1


res = Solution().numIslands_dfs(grid=[
    ["1", "1", "0", "0", "1"],
    ["1", "1", "1", "0", "0"],
    ["0", "0", "1", "1", "0"],
    ["0", "0", "0", "1", "1"]
])
print(res)
