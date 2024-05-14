from typing import List
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        left_to_r = [0 for _ in range(len(height))]
        right_to_l = [0 for _ in range(len(height))]
        max_left = 0
        max_right = 0
        res = 0
        for i in range(len(height)):
            max_left = max(max_left, height[i])
            left_to_r[i] = max_left
        for i in range(len(height))[::-1]:
            max_right = max(max_right, height[i])
            right_to_l[i] = max_right
        for i in range(len(height)):
            res += min(left_to_r[i], right_to_l[i]) - height[i]
        return res

    def trap2(self, height: List[int]) -> int:
        max_left, max_right = height[0], height[-1]
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            max_left = max(max_left, height[l])
            max_right = max(max_right, height[r])
            if height[l] <= height[r]: # 左向右
                ans += min(max_left,max_right) - height[l]
                l +=1
            else:
                ans += min(max_left,max_right) - height[r]
                r -=1
        return ans

    def trap3(self, height: List[int]) -> int: # 单调栈  栈里元素，上面>=后面元素，
        stack = deque()
        cur = 0
        ans =0
        #stack.append(0)
        # 核心思想是： 根据cur当前墙，找到上一面可以跟它匹配的墙(高度小于等于当前)
        while cur<=len(height)-1:
            while stack and height[stack[-1]]<height[cur]:
                check_idx = stack.pop()
                high = height[check_idx] # 需要计算面积的底
                while stack and height[stack[-1]] == high:
                    stack.pop()
                if not stack:break
                width = cur - stack[-1] -1
                high_now = min(height[cur],height[stack[-1]]) - high
                ans += width*high_now
            stack.append(cur)
            cur +=1
        return ans







sol = Solution().trap3([3,2,1,0,1,1,5])
print(sol)
