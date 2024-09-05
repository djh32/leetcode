# coding=utf-8
from typing import List
"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数 。

示例 1：
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

示例 2：
输入：s = "a"
输出：0

示例 3：
输入：s = "ab"
输出：1

提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成
"""

class Solution:

    def make_back_str_matrix(self,s:str):
        n = len(s)
        self.m = [[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                self.m[i][j] = (s[i] == s[j]) and self.m[i+1][j-1]
    def judge(self,idx1,idx2):
        return self.m[idx1][idx2]
    def minCut(self, s: str) -> int:
        self.make_back_str_matrix(s)
        n = len(s)
        dp = [float("inf")]*len(s)
        dp[0] = 0
        for i in range(n):
            for j in range(i+1,n):
                if self.judge(0,j):
                    dp[j]=0
                elif self.judge(i+1,j):
                    dp[j] = min(dp[i]+1,dp[j])
        return dp[-1]

print(Solution().minCut("abacdcr1234sdfcdcr1234sdfaba"))