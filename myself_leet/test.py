#coding=utf-8

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid) , len(grid[0])

        def recur(i, j):
            if  i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1':
                return False
            grid[i][j] = '0'
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                recur(ni, nj)
        cnt =0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    recur(i,j)
                    cnt +=1
        return cnt

print(Solution().numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))