import sys
from typing import List, Optional

"""

在 rows x cols 的网格上，你从单元格 (rStart, cStart) 面朝东面开始。网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。

你需要以顺时针按螺旋状行走，访问此网格中的每个位置。每当移动到网格的边界之外时，需要继续在网格之外行走（但稍后可能会返回到网格边界）。

最终，我们到过网格的所有 rows x cols 个空间。

按照访问顺序返回表示网格位置的坐标列表。


输入：rows = 1, cols = 4, rStart = 0, cStart = 0
输出：[[0,0],[0,1],[0,2],[0,3]]


"""


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        need_check_valid = rows * cols
        check_num = 0
        step = 1
        res = []

        check_num = self.is_valid_append(rStart, cStart, rows, cols,res,check_num) # 第一个位置的判断

        while check_num < need_check_valid:
            for _ in range(step):
                cStart += 1
                check_num =self.is_valid_append(rStart, cStart, rows, cols,res,check_num)
            for _ in range(step):
                rStart +=1
                check_num =self.is_valid_append(rStart, cStart, rows, cols,res,check_num)
            step += 1

            for _ in range(step):
                cStart -= 1
                check_num =self.is_valid_append(rStart, cStart, rows, cols,res,check_num)
            for _ in range(step):
                rStart -=1
                check_num =self.is_valid_append(rStart, cStart, rows, cols,res,check_num)
            step += 1
        return res

    def is_valid_append(self,r,c,row_len,col_len,res,check_num):
        if 0 <= r < row_len and 0 <= c < col_len:
            res.append([r,c])
            return check_num + 1
        return check_num

#matrix = [[1,2,3]  for _ in range(2)]

print(Solution().spiralMatrixIII(3,3,1,1))



