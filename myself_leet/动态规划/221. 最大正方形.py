# coding=utf-8
from typing import List
"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row,col = len(matrix),len(matrix[0])
        dp = [([0] * (col+1)) for _ in range(row+1)]
        res = 0
        for i in range(row):
            for j in range(col):
                dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j])+1 if matrix[i][j]=="1" else 0
                res = max(dp[i+1][j+1],res)
        return res*res

    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        row,col = len(matrix),len(matrix[0])
        dp = [([0] * col) for _ in range(row)]
        res = 0
        for i in range(row):
            for j in range(col):
                if i==0 or j ==0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1 if matrix[i][j]=="1" else 0
                res = max(dp[i][j],res)
        return res*res

print(Solution().maximalSquare2([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))




