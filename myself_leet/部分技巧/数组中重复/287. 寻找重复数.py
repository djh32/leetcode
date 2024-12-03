import sys
from typing import List, Optional

"""
287. 寻找重复数

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
"""
# class Solution {
# public:
#     int findDuplicate(vector<int>& nums) {
#         int tmp=0;
#         while(1){
#             tmp = nums[0];
#             swap(nums[0], nums[nums[0]]);
#             if(nums[0] == tmp) return tmp;
#         }
#
#     }
# };

class Solution:
    def findDuplicate(self, nums: List[int]) -> int: # 方法1
        while True:
            tmp = nums[0]

            holder = nums[nums[0]]
            nums[nums[0]] = nums[0]
            nums[0] = holder
            print(nums)
            if nums[0] == tmp:
                return nums[0]

    def findDuplicate2(self, nums: List[int]) -> int:
        n, i = len(nums), 0
        while i < n:
            t, idx = nums[i], nums[i] - 1
            if nums[idx] == t:
                if idx != i:
                    return t
                i += 1
            else:
                nums[i], nums[idx] = nums[idx], nums[i]
        return -1

    def findDuplicate3(self, nums: List[int]) -> int: # 2的平替版本，更好理解
        n, i = len(nums), 0
        for i in range(n):
            while nums[i] != i-1:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                holder = nums[nums[0]]
                nums[nums[0]] = nums[0]
                nums[0] = holder

            #nums[i],nums[nums[i]] = nums[nums[i]], nums[i]
print(Solution().findDuplicate3([2,1,3,2]))


"""

bool hasDuplicate(std::vector<int>& nums) {
    int n = nums.size();
    for (int i = 0; i < n; ++i) {
        while (nums[i] != i) {
            if (nums[i] == nums[nums[i]]) {
                return true; // 发现重复的数字
            }
            // 将当前元素放到它应该在的位置上
            std::swap(nums[i], nums[nums[i]]);
        }
    }

"""