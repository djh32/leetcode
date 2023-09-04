
## 题目地址(11. 盛最多水的容器)
from typing import  List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0
        while l<r :
            area_now = min(height[l],height[r])
            res = max(res,(r-l)*area_now)
            if height[r] > height[l]:
                l +=1
            else:
                r -=1
        return res


print(Solution().maxArea([1,2,4,6,26,84,34,5,2]))