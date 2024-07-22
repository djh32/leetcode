# coding=utf-8
import collections


class Solution:
    def __init__(self):
        self.ans = float("inf")

    def continue_words(self, s: str, begin_index: int):
        end_index = begin_index
        while end_index < len(s) and s[end_index] == s[begin_index]:
            end_index += 1
        return begin_index, end_index

    def findMinStep(self, board: str, hand: str) -> int:
        counter = collections.Counter(hand)  # dict

        def backtrack(board, counter, use_hand):
            if board == "" or use_hand == 5:
                self.ans = min(self.ans, use_hand)
                return

            i = 0
            while i < len(board):
                begin, end = self.continue_words(board, i)
                need = 3 - (end - begin)
                if need <= counter[board[begin]]:  # 必须用counter counter 对没有的key兼容0 改成dict就不行了。
                    # 当需要的数量小于当前hand有的，就能进入
                    need = max(0, need)
                    counter[board[i]] -= need
                    backtrack(board[:begin] + board[end:], counter, use_hand + need)
                    counter[board[i]] += need
                i = end

            # i = 0
            # while i < len(board):  # 情况考虑的不太对，应该先考虑need几个
            #     begin, end = self.continue_words(board, i)
            #     if end - begin >= 3:
            #         # 自然删除
            #         backtrack(board[:begin] + board[end:], counter, use_hand)
            #     elif board[i] in counter and counter[board[i]] > 0:
            #         # 干预删除
            #         if end - begin + counter[board[i]] >= 3:
            #             need = 3 - (end - begin)
            #             counter[board[i]] -= need
            #             backtrack(board[:begin] + board[end:], counter, use_hand + need)
            #             counter[board[i]] += need
            #     i = end

        backtrack(board, counter, 0)
        return -1 if self.ans == float("inf") else self.ans


print(Solution().findMinStep("RRWWRRW", "RR"))
