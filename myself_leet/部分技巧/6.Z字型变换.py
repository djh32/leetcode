# coding=utf-8
"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        length = len(s) - 1
        idx = 0
        while idx <= length:
            up_down = 0
            while idx <= length and up_down < numRows:
                res[up_down].append(s[idx])
                idx += 1
                up_down += 1
            down_up = numRows - 2
            while idx <= length and down_up > 0:
                res[down_up].append(s[idx])
                idx += 1
                down_up -= 1
        return "".join(["".join(sub) for sub in res])


class Solution2():
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        flag = -1
        res = ["" for _ in range(numRows)]
        i = 0
        for subs in s:
            res[i] +=subs
            if i ==0 or i ==numRows-1: flag=-flag
            i += flag
        return "".join(res)


print(Solution().convert("PAYPALISHIRING", 5))
print(Solution2().convert("PAYPALISHIRING", 5))
