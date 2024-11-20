from typing import List
from copy import deepcopy

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
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(board, row, col, rowlen, collen):
            if row == rowlen or row < 0 or col == collen or col < 0 or board[row][col] == '':  # bad case
                return False
            return True

        def backtracking(board, row, col, rowlen, collen, words):
            if len(words) == 0:
                return True
            if not valid(board, row, col, rowlen, collen):
                return False
            word = words[0]
            if word != board[row][col]:
                return False

            leave = words[1:]
            char = board[row][col]
            board[row][col] = ''
            res = False
            for deltarow, deltacol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                res = res or backtracking(board, row + deltarow, col + deltacol, rowlen, collen, leave)
            board[row][col] = char
            return res

        res = False
        rowlen = len(board)
        collen = len(board[0])
        for row in range(rowlen):
            for col in range(collen):
                res = res or backtracking(board, row, col, rowlen, collen, word)
        return res

    def exist_test(self, board: List[List[str]], word: str) -> bool:
        self.row_len = len(board)
        self.col_len = len(board[0])

        def dfs_check(board, tar, now, r, c):
            if tar == now:
                return True
            if len(now) > len(tar):
                return False
            if len(now) > 0 and now[-1] != tar[len(now) - 1]:
                return False
            holder = board[r][c]
            board[r][c] = None
            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r + i < self.row_len and 0 <= c + j < self.col_len and board[r + i][c + j] != None:
                    loop_check = dfs_check(board, tar, now + board[r + i][c + j], r + i, c + j)
                    if loop_check:
                        return True
                    else:
                        continue
            board[r][c] = holder

            return False

        for row in range(len(board)):
            for cow in range(len(board[0])):
                if dfs_check(board, word, board[row][cow], row, cow) == True: return True
        return False

    def exist_good(self, board: List[List[str]], word: str) -> bool:
        rowlen = len(board)
        collen = len(board[0])

        def dfs(i, j, k) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:  # 匹配成功！
                return True
            holder = board[i][j]
            board[i][j] = None
            for (r, c) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= r < rowlen and 0 <= c < collen and dfs(r,c,k+1):
                    return True

            board[i][j] = holder
            return False


        for row in range(len(board)):
            for cow in range(len(board[0])):
                if dfs(row, cow, 0) == True:
                    return True
        return False


print(Solution().exist_good([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCE"))
