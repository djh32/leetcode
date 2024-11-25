from typing import List


class Solution:
    def bin_serch(self, nums: List[int]):
        l, r = 0, len(nums) - 1
        pex = nums[l]
        while l < r:
            while r > l and nums[r] >= pex:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= pex:
                l += 1
            nums[r] = nums[l]
        nums[l] = pex
        return len(nums[l:])

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        res = 1
        first_order = sorted(envelopes, key=lambda x: (x[0], x[1]))
        sec_order = [x[1] for x in first_order]
        for idx,nums in enumerate(sec_order):
            if idx + 1 < len(sec_order) and sec_order[idx]==sec_order[idx+1]:
                continue
            res = max(res, self.bin_serch(sec_order[idx:]))
        return res


print(Solution().maxEnvelopes([[1,1],[1,1],[1,1]]))