# coding=utf-8
from typing import List
# [0,1,2,3,4,5]

import collections
'''
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
'''

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        length = len(s)
        res = dict()
        i = 0
        while i <= length - minSize:
            now_str = s[i:i+minSize]
            if len(set(now_str)) >=maxLetters:
                if now_str not in res:
                    res[now_str] = 0
                res[now_str] += 1
            i +=1

        return max(res.values()) if res else 0

print(Solution().maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))

