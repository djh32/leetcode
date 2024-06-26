from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(left, right, now):
            if left < 0 or right < 0:
                return
            if left == 0 and right == 0:
                res.append(now)
                return
            if left > right:
                return
            dfs(left - 1, right, now + '(')
            dfs(left, right - 1, now + ')')

        dfs(n, n, "")
        return res


print(Solution().generateParenthesis(3))
