from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        n = len(nums)
        prefix = 1
        for i in range(n):
            r.append(prefix)
            prefix *= nums[i]
        suffix = 1
        for i in reversed(range(n)):
            r[i]*=suffix
            suffix *= nums[i]
        return r
