# Definition for singly-linked list.
from typing import List
class Solution:  # 递归反转
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        pos_end = m + n - 1
        while pos_end >= 0 and m-1>=0 and n-1 >=0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[pos_end] = nums1[m - 1]
                m -= 1
            else:
                nums1[pos_end] = nums2[n - 1]
                n -= 1
            pos_end -= 1
        while n-1>=0:
            nums1[pos_end] = nums2[n - 1]
            n -=1
            pos_end -= 1
        return nums1


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        end = m + n - 1
        if m == 0:
            nums1[0] = nums2[0]
        n = n - 1
        m = m - 1

        while n >= 0 and m >= 0:
            # print nums1,m,n,end
            if nums1[m] >= nums2[n]:
                nums1[end] = nums1[m]
                m -= 1
            else:
                nums1[end] = nums2[n]
                n -= 1
            end -= 1
        # if m ==-1:
        #    for i in range(n+1):
        #        nums1[i] = nums2[i]
        nums1[:n + 1] = nums2[:n + 1]

        # print nums1,m,n,end




