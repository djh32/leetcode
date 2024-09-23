import sys
from typing import List, Optional

# 汇量科技，2024.09.11遇到
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        if not m: return m
        res = []
        l, r, top, down = 0, len(m[0]) - 1, 0, len(m) - 1
        while True:
            for i in range(l, r + 1):
                res.append(m[top][i])
            top += 1
            if top > down: break
            for i in range(top, down + 1):
                res.append(m[i][r])
            r -= 1
            if r < l: break
            for i in range(r, l - 1, -1):
                res.append(m[down][i])
            down -= 1
            if top > down: break
            for i in range(down, top - 1, -1):
                res.append(m[i][l])
            l += 1
            if r < l: break
        return res


m = [[1, 2, 3, 2], [4, 5, 6, 1], [7, 8, 9, 3]]
e = Solution().spiralOrder(m)
print(e)
