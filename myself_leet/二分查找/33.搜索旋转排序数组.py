# coding=utf-8
from typing import List

'''class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int mid = (left + right) >> 1;
            if (nums[mid] == target) return mid;
            if (nums[left] <= nums[mid]) {
                // left 到 mid 是顺序区间
                (target >= nums[left] && target < nums[mid]) ? right = mid - 1 : left = mid + 1;
            }
            else {
                // mid 到 right 是顺序区间
                (target > nums[mid] && target <= nums[right]) ? left = mid + 1 : right = mid - 1;
            }
        }
        return -1;
    }
};'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:  # 重点在于这个等号是引入，不是判断，这里如果没有= 则下面的=就没用了。 可以把等号去掉使用 print(Solution().search([4,5,6,7,0,1,2], 3)) 走一边case就知道了
                # mid 左边有序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] >= nums[mid]:
                # mid - r 右边有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


print(Solution().search([4,5,6,7,0,1,2], 3))

'''
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 
在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
'''


