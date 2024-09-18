import sys
from typing import List, Optional
"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        自己写的逻辑有问题。 不能和螺旋矩阵一样，找不动index不变的方式去update，否则中间的逻辑会出错。
        """

        l,n = 0,len(matrix)-1
        while l<=n:
            for i in range(l,n):
                matrix[i][n],matrix[n][n-i],matrix[n-i][l],matrix[l][i] = matrix[l][i],matrix[i][n],matrix[n][n - i],matrix[n-i][l]
            l +=1
            n -=1
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        需要考虑奇数、偶数的长度
        :param matrix:
        :return: None
        """
        n = len(matrix) # 方矩阵
        for i in range(n//2):
            for j in range((n+1) // 2): # 这里重点
                # matrix[j][n-1-i]= matrix[i][j]
                # matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                # matrix[n-1-j][i] =matrix[n-1-i][n-1-j]
                # matrix[i][j]=matrix[n-1-j][i]
                matrix[j][n - 1 - i],matrix[n-1-i][n-1-j],matrix[n-1-j][i],matrix[i][j] = matrix[i][j],matrix[j][n-1-i],matrix[n-1-i][n-1-j],matrix[n-1-j][i]










m = [[1, 2, 3, 4,5], [4, 5, 6, 7,8], [6,7, 8, 9, 10],[2,3,4,5,6],[1,1,2,2,3]]
m = [[1, 2, 3, 5], [4,  6, 7,8],[2,3,4,6],[1,2,2,3]]

Solution().rotate(m)
print(m)
