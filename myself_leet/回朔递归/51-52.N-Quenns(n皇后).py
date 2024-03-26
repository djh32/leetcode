from typing import List

'''
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }
    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}

作者：代码随想录
链接：https://leetcode.cn/problems/n-queens/solutions/2566744/dai-ma-sui-xiang-lu-leetcode51nhuang-hou-hcat/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board_real = [['.'] * n for _ in range(n)]
        res = []

        def valid(board, row, col) -> bool:
            # 左上角
            t_row = row
            t_col = col
            while t_row > 0 and t_col > 0:
                t_row -= 1
                t_col -= 1
                if board[t_row][t_col] == 'Q':
                    return False
            # 右上角
            t_row = row
            t_col = col
            while t_row > 0 and t_col < n-1:
                t_row -= 1
                t_col += 1
                if board[t_row][t_col] == 'Q':
                    return False

            # 列
            t_row = row
            while t_row > 0:
                t_row -= 1
                if board[t_row][col] == 'Q':
                    return False

            return True

        def backtracking(board, row, col):
            if row == n:
                res.append(["".join(l) for l in board])
                return
            for col in range(n):
                if not valid(board, row, col):
                    continue  # row 是深度， 本层深度当前col的数据不满足则之后col不用遍历
                board[row][col] = 'Q'
                backtracking(board, row + 1, col)
                board[row][col] = '.'

        backtracking(board_real,0,n)

        return res


print(Solution().solveNQueens(8))
