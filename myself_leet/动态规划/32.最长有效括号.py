class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        i = 1
        res = 0
        while i < len(s):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2
                    if i >= 2:
                        dp[i] = 2 + dp[i - 2]
                else:  # i-1==")"
                    if dp[i - 1] > 0:  # i从1开始,且合规
                        if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":  # match
                            dp[i] = dp[i - 1] + 2
                            if i - dp[i - 1] - 2 >= 0:
                                dp[i] += dp[i - dp[i - 1] - 2]
            res = max(dp[i], res)
            i += 1
        return res


print(Solution().longestValidParentheses("()((())))"))
