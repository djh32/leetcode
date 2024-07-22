# coding=utf-8
from typing import List
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点  (i, ai) 。在坐标内画 n 条垂直线，垂直线 i  的两个端点分别为  (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与  x  轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且  n  的值至少为 2。

![11.container-with-most-water-question](https://p.ipic.vip/ia6rj3.jpg)

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为  49。

示例：
`
输入：[1,8,6,2,5,4,8,3,7]
输出：49
"""
class Solution:
    def maxArea(self, heights):
        l,r = 0,len(heights)-1
        max_area = 0
        while l<r: # ending l==r
            h = min(heights[l],heights[r])
            lens = r-l
            max_area = max(max_area,h*lens)
            if heights[l]>heights[r]:
                r -=1
            else:
                l +=1
        return max_area


print(Solution().maxArea([0,2]))
