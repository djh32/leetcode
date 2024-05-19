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