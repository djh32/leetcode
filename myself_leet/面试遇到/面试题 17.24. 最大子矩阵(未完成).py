#coding=utf-8
"""
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。
若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例：

输入：
[
   [-1,0],
   [0,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵
"""
from typing import List
# todo 待完成

class Solution:
    def get_pre_sum_matrix(self, matrix: List[List[int]]):
        row_len,col_len = len(matrix)+1,len(matrix[0])+1
        pre_sum_matrix = [[0]*col_len for _ in range(row_len)]
        for i in range(1,row_len):
            for j in range(1,col_len):
                pre_sum_matrix[i][j] = pre_sum_matrix[i-1][j] + pre_sum_matrix[i][j-1]-pre_sum_matrix[i-1][j-1] + matrix[i-1][j-1]
        #print(pre_sum_matrix)
        return pre_sum_matrix

    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        self.max = float("-inf")
        pre_sum = self.get_pre_sum_matrix(matrix)
        r_l,c_l = len(pre_sum),len(pre_sum[0])
        for top in range(1,r_l):
            for down in range(top,r_l):
                pass


        pass


Solution().get_pre_sum_matrix([[1,2,3],[2,1,1],[1,1,1]])


