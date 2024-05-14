from typing import List
from collections import deque
class Solution:

    def trap(self, height: List[int]) -> int: # 单调栈  栈里元素，上面>=后面元素，
        stack = deque()
        cur = 0
        ans =0
        # 核心思想是： 根据cur当前墙，找到上一面可以跟它匹配的墙(高度不小于等于当前)
        while cur<=len(height)-1:
            while stack and height[stack[-1]]<height[cur]:
                check_idx = stack.pop()
                high = height[check_idx] # 原堆栈顶的墙高（需要计算区域的真实高度，后面和min(height[cur],height[stack[-1]]) 做对比）
                while stack and height[stack[-1]] == high:
                    stack.pop()
                if not stack:break
                width = cur - stack[-1] -1 #现在实际栈顶是stack[-1]
                high_now = min(height[cur],height[stack[-1]]) - high
                ans += width*high_now
            stack.append(cur)
            cur +=1
        return ans







sol = Solution().trap3([3,2,1,0,1,1,5])
print(sol)
