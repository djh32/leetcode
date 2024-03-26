class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        multitime = 0
        res = ""
        for st in s:
            if st.isdigit():
                multitime = multitime*10 + int(st)
            elif st == '[':
                stack.append((res, multitime))
                res, multitime = '', 0
            elif st == ']':
                last_res, last_multi = stack.pop(-1)
                res = last_res + int(last_multi) * res
            else:
                res += st
        return res

print(Solution().decodeString("10[leetcode]"))

