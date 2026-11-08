class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n -1
        while left != right:
            lfsum = numbers[left]+numbers[right]
            if lfsum > target:
                right -=1
                continue
            
            if lfsum == target:
                return [left+1, right+1]
            
            left += 1
        
        return [0,0]
