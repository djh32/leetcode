class Solution:
    def countSubstrings(self, s: str) -> int:
        count_all = 0
        for i in range(len(s)):
            #count_all += 1 #下面加过了，再遍历到自己的时候进入函数处理即可。
            count_all += self.check_palindrome(s,i,i)
            count_all += self.check_palindrome(s,i,i+1)
        return count_all

    def check_palindrome(self, s: str, begin, end):
        length_touch = len(s) - 1
        count = 0
        while begin >= 0 and end <= length_touch and s[begin] == s[end]:
            begin -= 1
            end += 1
            count += 1 # 这里本身自己就+1了， 上面不用加了
        return count


res = Solution().countSubstrings("abaaa")
print(res)
