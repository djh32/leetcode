# coding=utf-8
from typing import List
import collections
class Solution:
    # readme的答案
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = collections.Counter(p)
        ans = []
        for i in range(len(s)):
            if i >= len(p):
                target[s[i - len(p)]] += 1
                if target[s[i - len(p)]] == 0:
                    del target[s[i - len(p)]]
            target[s[i]] -= 1
            if target[s[i]] == 0:
                del target[s[i]]
            if len(target) == 0:
                ans.append(i - len(p) + 1)
        return ans

class Solution:
    # 自己按照滑动窗口理解
    # 这里必须按照window里面总体计数，不能按照有无进行计算，逻辑不对
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = set(p)
        l,r = 0,0
        info = {}
        window_valid = 0
        res = []
        while r <len(s):
            if s[r] in p:
                if s[r] not in info:
                    info[s[r]] = 1
                    window_valid +=1
                elif info[s[r]] == 1: # 重复出现
                    pass
            while r-l==len(p)-1:
                if window_valid == len(p):
                    res.append(l+1)
                if s[l] in ans:
                    info[s[l]]-=1
                    window_valid -= 1
                    if info[s[l]] == 0:
                        del info[s[l]]
                l +=1
            r +=1
        if len(info)==window_valid:res.append(l+1)
        return res

class Solution2:
    # 自己按照滑动窗口理解
    # 这里很重要的是需要按照ans的大小进行判断，因为当info[s[r]] == ans[s[r]]的时候
    # 增加window里面的计数，只有window的计数等于ans的结果的时候
    # 匹配度window_valid 才能+1(一个字符匹配成功)， 且所有匹配度都满足的条件是window_valid == len(ans)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = collections.Counter(p)
        l,r = 0,0
        info = {}
        window_valid = 0
        res = []
        while r <len(s):
            if s[r] in ans:
                if s[r] not in info:
                    info[s[r]] = 1
                else:
                    info[s[r]] += 1
                if info[s[r]] == ans[s[r]]:
                    window_valid +=1
            while r-l==len(p)-1:
                if window_valid == len(ans):
                    res.append(l)
                if s[l] in ans:
                    if info[s[l]] == ans[s[l]]: # 窗口里面当前是合法的，但是由于size要变小，所以会变成不合法。
                        window_valid -= 1
                    info[s[l]]-=1
                l +=1
            r +=1
        return res

print(Solution2().findAnagrams(s='abaabaaaa', p='aba'))