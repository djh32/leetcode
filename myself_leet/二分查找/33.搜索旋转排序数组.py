
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
            mid = l + (r-l)// 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:  # 重点在于这个等号是引入，不是判断，这里如果没有= 则下面的=就没用了。
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

print(Solution().search([3,1],33))



