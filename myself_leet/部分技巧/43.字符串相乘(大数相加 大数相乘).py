# coding=utf-8
from typing import List

"""
big sum
"""


def big_sum(num1: List[int], nums2: List[int]) -> int:
    idx1, idx2 = len(num1) - 1, len(nums2) - 1
    res = []
    is_up = 0
    while idx1 >= 0 or idx2 >= 0 or is_up:
        i1 = num1[idx1] if idx1 >= 0 else 0
        i2 = nums2[idx2] if idx2 >= 0 else 0
        tmp = i1 + i2 + is_up
        if tmp >= 10: # 注意等于
            is_up = 1
        else:
            is_up = 0
        res.append(tmp % 10)
        idx1 -= 1
        idx2 -= 1
    res.reverse()
    res = [str(i) for i in res]
    res = int("".join(res))
    return res


print(big_sum([9, 2], [1,0]))

"""

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

 

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "4567"
输出: "56088"
"""


class Solution:
    def multiply(self,num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":return "0"
        sp = lambda x : [int(s) for s in x]
        num1, num2 = sp(num1), sp(num2)
        res = [0]

        for i in range(0,len(num1))[::-1]:
            tmp = [0] * (len(num1) - i -1)
            tmp = self.multi_one(num1[i],num2,tmp)
            res = self.big_sum(tmp,res)
            res = [int(i) for i in str(res)]
        return "".join([str(x) for x in res])

    def multi_one(self,n1: int, n2: List[int], tmp) -> List[int]:
        res = []
        upper = 0
        for i in range(len(n2) - 1, -1, -1):
            tmp_res = n1 * n2[i] + upper
            upper = tmp_res // 10
            res.append(tmp_res % 10)
        if upper > 0:
            res.append(upper)
        tmp.extend(res)
        tmp.reverse()
        return tmp

    def big_sum(self,num1: List[int], nums2: List[int]) -> int:
        idx1, idx2 = len(num1) - 1, len(nums2) - 1
        res = []
        is_up = 0
        while idx1 >= 0 or idx2 >= 0 or is_up:
            i1 = num1[idx1] if idx1 >= 0 else 0
            i2 = nums2[idx2] if idx2 >= 0 else 0
            tmp = i1 + i2 + is_up
            if tmp >= 10:  # 注意等于
                is_up = 1
            else:
                is_up = 0
            res.append(tmp % 10)
            idx1 -= 1
            idx2 -= 1
        res.reverse()
        res = [str(i) for i in res]
        res = int("".join(res))
        return res


print(Solution().multiply("999","11"))











