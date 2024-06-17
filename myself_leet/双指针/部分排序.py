# coding=utf-8
from typing import List
'''
给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。
输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
输出： [3,9]
'''

class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        left, right = -1,-1
        max_cache = float("-inf")
        min_cache = float("inf")
        for i in range(len(array)):
            max_cache = max(max_cache, array[i])
            if array[i] < max_cache:
                right = i
        for i in range(len(array)-1,-1,-1):
            min_cache = min(min_cache, array[i])
            if array[i] > min_cache:
                left = i
        return [left,right]
print(Solution().subSort([1,9,2]))