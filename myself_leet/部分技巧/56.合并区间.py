from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st_interval = sorted(intervals,key=lambda a:a[0]) #nlogn
        i = 0
        while i < len(st_interval):
            if i +1 < len(st_interval) and st_interval[i+1][0] <= st_interval[i][1]:
                left = st_interval.pop(i)
                right = st_interval.pop(i)
                max_right = max(right[1],left[1]) # 不能只用右的， 因为 [1,3][1,10] 放大了右边，不一定右边的最大。 再和[2,6] 比较
                new = [left[0],max_right]
                st_interval.insert(i,new)
                i -=1
            i +=1
        return st_interval


sol = Solution().merge([[1,3],[2,6],[1,10],[15,18]])
print (sol)