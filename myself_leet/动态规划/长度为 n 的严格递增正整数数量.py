# coding=utf-8
# 给定一个整数 n，返回长度为 n 的数字严格递增的正整数的数量。
# 没有原题是点赞的题目

class Solution:
    def solve(self, n):
        dp = [[0] * 10 for _ in range(n)]
        dp[0] = [0] + [1] * 9

        for i in range(1, n):
            for j in range(1, 10):
                for k in range(j):
                    dp[i][j] += dp[i - 1][k]
        return sum(dp[-1])

print(Solution().solve(3))


