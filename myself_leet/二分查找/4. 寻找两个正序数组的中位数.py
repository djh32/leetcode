# coding=utf-8
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        low, high = 0, nums1_len

        while low <= high:
            mid1 = int(low + high / 2)
            mid2 = int((nums2_len + nums1_len + 1) / 2 - mid1)
            # 重点这里 (mid1 + mid2 = (nums2_len + nums1_len + 1) / 2 - mid1)
            # 带约束的二分查找，仅查找短数组即可

            left1 = float("-inf") if mid1 == 0 else nums1[mid1 - 1]
            right1 = float("inf") if mid1 == nums1_len else nums1[mid1]

            left2 = float("-inf") if mid2 == 0 else nums2[mid2 - 1]
            right2 = float("inf") if mid2 == nums2_len else nums2[mid2]

            if left1 <= right2 and left2 <= right1:
                if (nums1_len + nums2_len) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                return max(left1, left2)  # nums1_len+nums2_len 奇数个
            else:
                if left1 > right2:
                    high = mid1 - 1
                else:
                    low = mid1 + 1
        return -1


print(Solution().findMedianSortedArrays([1, 2, 10, 24, 25], [1, 2, 5, 6, 7]))
