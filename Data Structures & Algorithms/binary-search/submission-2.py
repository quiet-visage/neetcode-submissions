class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n-1

        while start <= end:
            pivot = start + (end-start) // 2
            elem = nums[pivot]
            if elem == target:
                return pivot
            if elem > target:
                end = pivot - 1
            if elem < target:
                start = pivot + 1


        return -1