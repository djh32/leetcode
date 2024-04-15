from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def recur(cur,tar,step):
            if nums[cur] ^ nums[tar] <0: # xor
                return False
            if cur == tar and cur in visited and step >1: return True
            if cur in visited:return False
            visited.add(cur)
            if nums[cur] >0:
                return recur((cur + nums[cur]) % n, tar, step+1)
            else:
                return recur((cur + nums[cur]) % n, tar, step+1)
        n = len(nums)
        visited = None
        for i in range(len(nums)):
            visited = set()
            if recur(i,i,0):
                return True
        return False

print(Solution().circularArrayLoop([2,-2,1,3,-3]))
