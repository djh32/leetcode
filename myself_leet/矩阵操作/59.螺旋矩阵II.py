import sys
from typing import List, Optional

"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]


"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]

        l, r, t, d = 0, n, 0, n
        num = 1
        while num < n * n + 1:
            for i in range(l, r):
                res[t][i] = num
                num += 1
            t += 1
            for i in range(t, d):
                res[i][r - 1] = num
                num += 1
            r -= 1
            for i in range(r - 1, l - 1, -1):
                res[d - 1][i] = num
                num += 1
            d -= 1
            for i in range(d - 1, t - 1, -1):
                res[i][l] = num
                num += 1
            l += 1

        return res


print(Solution().generateMatrix(5))
