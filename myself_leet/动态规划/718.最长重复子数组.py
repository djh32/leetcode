# coding=utf-8
from typing import List


class Solution:
    def findLength(self, A: List, B: List):
        size_a = len(A)
        size_b = len(B)
        loader = [[0 for _ in range(size_b)]for _ in range(size_a)]  # A*B
        max_res = 0
        for i in range(size_a):
            for j in range(size_b):
                if i>0 and j >0 and A[i]==B[j]:
                    loader[i][j] = loader[i-1][j-1] +1
                    max_res = max(loader[i][j],max_res)
                if (i==0 or j ==0) and A[i]==B[j]:
                    loader[i][j] = 1
        return max_res


print(Solution().findLength([3,2,1,3],[2,1,3]))
