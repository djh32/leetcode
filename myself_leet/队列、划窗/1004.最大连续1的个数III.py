from typing import List

# 滑动窗口可以用两个for循环，也可以用空间换取时间。

class Solution:
    # 空间
    def longestOnes(self, nums: List[int], k: int) -> int:
        cache_list = []
        l, r = 0, 0
        res = 0
        while r < len(nums):
            if nums[r] == 0:
                cache_list.append(r) #只有0能进入
                if len(cache_list) > k:
                    # 通过改变l，删除窗口最左边第一个0元素。使窗口维持最多k个
                    # 这里拉爆了窗口，那么从窗口第一个位置的下一个位置开始作为l重新计算
                    # 举例111000 k=2 的时候在r=5时候爆，另l=4从新观察就行了
                    l = cache_list.pop(0) + 1
            res = max(r - l + 1, res)
            r +=1
        return res


class Solution(object):
    #时间
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        l, r = 0, 0
        res = 0
        zerowind = 0
        while r < len(A):
            if A[r] == 0:
                zerowind += 1

            while zerowind > K:
                if A[l] == 0:
                    zerowind -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
            # print r-1,l,res
        return res

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0],k=2))