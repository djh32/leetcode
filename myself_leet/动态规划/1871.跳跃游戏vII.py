# coding=utf-8
from typing import List

"""
给你一个下标从 0 开始的二进制字符串 s 和两个整数 minJump 和 maxJump 。一开始，你在下标 0 处，且该位置的值一定为 '0' 。当同时满足如下条件时，你可以从下标 i 移动到下标 j 处：

i + minJump <= j <= min(i + maxJump, s.length - 1) 且
s[j] == '0'.

如果你可以到达 s 的下标 s.length - 1 处，请你返回 true ，否则返回 false 。

 

示例 1：

输入：s = "011010", minJump = 2, maxJump = 3
输出：true
解释：
第一步，从下标 0 移动到下标 3 。
第二步，从下标 3 移动到下标 5 。

示例 2：

输入：s = "01101110", minJump = 2, maxJump = 3
输出：false

提示：

2 <= s.length <= 105
s[i]要么是'0'，要么是'1'
s[0] == '0'
1 <= minJump <= maxJump < s.length
"""


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # 超时
        dp = [1] + [0] * (len(s) - 1)
        for i in range(minJump,len(s)): # 这里的minjump需要，不能从1开始。
            now_reach = s[i]=='0' and any(dp[max(0,i-maxJump):max(0,i-minJump)+1])
            if now_reach:
                dp[i]=1
        print(dp)
        return True if dp[-1] else False


print(Solution().canReach("0000000000", minJump=2, maxJump=5))
