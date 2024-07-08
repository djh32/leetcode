# coding=utf-8
from typing import List

"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

示例 2：
输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
import collections


# 和438题类似的题目，不过需要找到最小的串，438找固定长度的合法窗口。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        ans = collections.Counter(t)
        window_info = {}
        l, r = 0, 0
        valid = 0
        while r < len(s):
            if s[r] not in window_info:
                window_info[s[r]] = 1
            else:
                window_info[s[r]] += 1
            if window_info[s[r]] == ans[s[r]]:
                valid += 1

            while valid == len(ans):
                # 考虑好滑窗口的更新状态。
                res = s[l:r + 1] if len(s[l:r + 1]) <= len(res) or res == "" else res  # min res
                if s[l] in ans:
                    # 这里最重要，当s[l]窗口左侧是需要判定的字符串的时候，
                    # 如果当前window下该字符串满足条件，（满足条件意味着window_info[s[l]] == ans[s[l]]）窗口中要删除字符的数量等于合法数量
                    # 变为不合法，同时需要减少1然后结束缩窗的判断。
                    if window_info[s[l]] == ans[s[l]]:
                        valid -= 1
                    window_info[s[l]] -= 1
                l += 1
            r += 1
        return res


print(Solution().minWindow("ab", "b"))
