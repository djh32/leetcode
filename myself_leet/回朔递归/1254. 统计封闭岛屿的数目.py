# coding=utf-8
from typing import List

"""
二维矩阵 grid 由 0 （土地）和 1 （水）组成。岛是由最大的4个方向连通的 0 组成的群，封闭岛是一个 完全 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

 
"""


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        row = len(grid)
        col = len(grid[0])

        def recur_find_island(i, j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            if grid[i][j] == 1:
                return True
            if grid[i][j] == 0:
                grid[i][j] =1
            up = recur_find_island(i - 1, j)
            down = recur_find_island(i + 1, j)
            left = recur_find_island(i, j - 1)
            right = recur_find_island(i, j + 1)
            return up and  down and left and right

        for i in range(row):
            for j in range(col):
                if grid[i][j]==0 and recur_find_island(i, j):
                    res += 1
        return res


res = Solution().closedIsland(grid=[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
print(res)
