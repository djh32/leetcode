from copy import deepcopy
# 困难题：从头到位没看解答，自己写的，写了他妈一小时。
class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        self.res = ""
        cache = []
        left = list(range(1, n + 1))

        def recur(left: list, k: int, tmp: list) -> str:
            if not left:
                self.res = deepcopy(tmp)
                return
            multi_accum = 1
            for i in range(1, len(left) + 1):
                multi_accum *= i
            sheld = [multi_accum / len(left) * i for i in range(1,len(left)+1)]  # [6,12,18,24]  如果k 大于里面的第一个，说明走了至少6步以上，换开头了，如果没到6，那么就是1开头。
            for i in range(len(left)):
                if k <=sheld[i]: break
            tmp.append(left.pop(i))
            recur(left, k - sheld[i-1] if i >0 else k, tmp)  # 这里是重点， 有可能越界，如果越界说明k不足一个区间（multi_accum / len(left)）的步数，所以用k继续透传下去

        recur(left,k,cache)
        return "".join([str(i) for i in self.res])

class Solution2: # 官方答案
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        k -= 1
        ans = list()
        valid = [1] * (n + 1)
        for i in range(1, n + 1):
            order = k // factorial[n - i] + 1
            for j in range(1, n + 1):
                order -= valid[j]
                if order == 0:
                    ans.append(str(j))
                    valid[j] = 0
                    break
            k %= factorial[n - i]

        return "".join(ans)

import math
class Solution3: # readme 解答
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        candidates = [str(i) for i in range(1, n + 1)]

        while n != 0:
            facto = math.factorial(n - 1)
            # i 表示前面被我们排除的组数，也就是k所在的组的下标
            # k // facto 是不行的， 比如在 k % facto == 0的情况下就会有问题
            i = math.ceil(k / facto) - 1
            # 我们把candidates[i]加入到结果集，然后将其弹出candidates（不能重复使用元素）
            res += candidates[i]
            candidates.pop(i)
            # k 缩小了 facto *  i
            k -= facto * i
            # 每次迭代我们实际上就处理了一个元素，n 减去 1，当n == 0 说明全部处理完成，我们退出循环
            n -= 1
        return res

print(Solution3().getPermutation(4,9))