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
            for deltarow,deltacol in [(-1,0),(1,0),(0,-1),(0,1)]:
                res = res or backtracking(board,row+deltarow,col+deltacol,rowlen,collen,leave)
            board[row][col] = char
            return res

        res = False
        rowlen = len(board)
        collen = len(board[0])
        for row in range(rowlen):
            for col in range(collen):
                res = res or backtracking(board, row, col, rowlen, collen, word)
        return res

print(Solution().exist([['c','e'],['c','s'],['e','e']], "csec"))