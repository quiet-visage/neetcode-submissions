class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        trct = nums
        trct = list({*trct})
        trct.sort()
        n = len(trct)
        result = 1
        acc = 1
        left = 0
        i = 1
        while i < n:
            is_seq = (trct[i] - trct[i-1]) == 1
            if is_seq:
                acc+=1
                result = max(result, acc)
            else:
                acc = 1
            i+=1
        print(trct)
        return result
