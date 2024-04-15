# 两种方法，
# 方法1：和647题找全部回文一样，只不过对比奇数、偶数个中心的大小，并且记录位置
# 方法2就是dp解决，空间换时间。  dp[][]   i,j 表示 i-j之间是回文。

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_is_palindrome(s, begin, end):
            touch_len = len(s) - 1
            while begin >= 0 and end <= touch_len and s[begin] == s[end]:
                begin -= 1
                end += 1
            return begin + 1, end - begin - 1  # [left,right) #这个返回很重要，确定返回一定是回文，并且确定回文的长度以及起始方便后面对比

        res = [0, 0]
        for i in range(len(s)):
            a, b = check_is_palindrome(s, i, i)
            a2, b2 = check_is_palindrome(s, i, i + 1)
            max_idx, max_len = (a, b) if b > b2 else (a2, b2)
            if max_len > res[1]:
                res[0] = max_idx
                res[1] = max_len
        return s[res[0]:res[0] + res[1]]

    def longestPalindrome2(self, s: str) -> str:
        sz = len(s)
        # 细节1
        if sz < 2:
            return s
        # 生成两个for
        tmp = [[False for _ in range(sz)] for _ in range(sz)]
        for i in range(sz):
            tmp[i][i] = True
        max_len = 1  # 对于长度>2的串最小肯定是1。
        # res = (0, 0) # 注意这种题就别用尾巴了，直接用begin和长度找子串就行，因为case : "ac" 如果用尾的话会导致不进入循环，不更新了for循环的尾部导致出错。
        begin = 0
        for j in range(1, sz):
            for i in range(j):
                # 多种状态的判定， 从上到下遍历，而不是左到右。 大体分为两种，如果长度小于2，只看首尾是否相同。
                # 否则需要判断tmp[i+1][j-1]是否是回文。
                if j - i - 1 < 2 and s[i] == s[j]:  # 如果长度小于2的字符串 首尾相同
                    tmp[i][j] = True
                elif j - i - 1 >= 2 and s[i] == s[j] and tmp[i + 1][j - 1] == True:
                    tmp[i][j] = True
                if tmp[i][j] == True and j - i + 1 >= max_len:
                    max_len = j - i + 1
                    res = (i, j)
                    begin = i
        # return s[res[0]:res[1]+1]
        return s[begin:begin + max_len]


x = Solution().longestPalindrome2("aasdfaaaavvvaaaasdfssc")
print(x)

# for i in x:
#    print(i)
