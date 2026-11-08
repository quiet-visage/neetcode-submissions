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

        for i in range(1, n):
            is_seq = (trct[i] - trct[i - 1]) == 1
            if is_seq:
                acc += 1
                result = max(result, acc)
                continue
            acc = 1

        return result
