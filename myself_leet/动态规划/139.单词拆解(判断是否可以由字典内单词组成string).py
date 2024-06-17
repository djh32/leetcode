# coding=utf-8
from typing import List
"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        cache_index = -1
        for index in range(len(s)):
            sub_str = s[:index+1]
            if cache_index >= 0 and s[cache_index+1:index+1] in wordDict:
                dp[index] = True
                cache_index = index
            if sub_str in wordDict:
                dp[index] = True
                cache_index = index
        return dp[-1]


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        #cache_index = -1
        for index in range(len(s)):
            sub_str = s[:index+1]
            if sub_str in wordDict:
                dp[index] = True
                continue

            for i in range(index):
                if dp[i] and s[i+1:index+1] in wordDict:
                    dp[index] = True
                    break

        return dp[-1]
print(Solution2().wordBreak(s = "abcd", wordDict=["a","b","abc","cd"]))
