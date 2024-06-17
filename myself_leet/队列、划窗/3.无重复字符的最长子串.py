# coding=utf-8

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        d = {}
        left= 0
        for i in range(len(s)):
            if s[i] in d:
                left = max(left,d[s[i]]+1)
            len_now = i - left + 1
            max_len = max(max_len,len_now)
            d[s[i]] = i
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        res = 0
        window_left = 0
        for i in range(len(s)):
            if s[i] not in cache:
                cache[s[i]] = i
            else:
                window_left = max(cache[s[i]] + 1,window_left)
                cache[s[i]] = i
            now_window = i - window_left + 1
            res = max(res,now_window)
        return res

print(Solution2().lengthOfLongestSubstring("abcgasdfabcaaaa"))
print(Solution().lengthOfLongestSubstring("abcgasdfabcaaaa"))
