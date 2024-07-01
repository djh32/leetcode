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
    def islandPerimeter(self, grid: List[List[str]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:  # illegal
                return 1
            if grid[i][j] == 0:
                return 1
            if grid[i][j] == 2: #have seen 这个不能回去是精髓，不需要额外开辟所有的空间。
                return 0
            grid[i][j] = 2
            num = 0
            num += dfs(i + 1, j)
            num += dfs(i - 1, j)
            num += dfs(i, j + 1)
            num += dfs(i, j - 1)
            return num

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    result = dfs(i, j)
        return result


res = Solution().islandPerimeter(grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(res)
