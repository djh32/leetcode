import sys
from typing import List, Optional

# 汇量科技，2024.09.11遇到
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:return matrix
        l=u=0
        r=len(matrix[0])-1
        d = len(matrix)-1
        res = []
        while True:
            for i in range(l,r):
                res.append(matrix[u][i])
            u +=1
            if u == d:break

            for i in range(u,d):
                res.append(matrix[i][r])
            r -=1
            if r == l: break

            for i in range(r,l-1,-1):
                res.append(matrix[d][i])
            d -=1
            if u == d: break

            for i in range(d,u-1,-1):
                res.append(matrix[i][l])
            l +=1
            if r == l: break
        return res
m = [[1, 2, 3, 2], [4, 5, 6, 1], [7, 8, 9, 3]]
e = Solution().spiralOrder(m)
print(e)
