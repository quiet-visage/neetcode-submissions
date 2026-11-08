class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for i in range(len(nums)):
            target = nums[i]

            if target in cache:
                return True

            cache[target] = i
        
        return False