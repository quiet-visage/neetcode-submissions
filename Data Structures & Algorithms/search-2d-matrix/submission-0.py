class Solution:
    def bsearch(self, array: List[int], target: int) -> bool:
        start, end = 0, len(array) - 1
        while start <= end:
            pivot = start + (end - start) // 2
            elem = array[pivot]
            if elem == target:
                return True
            if elem > target:
                end = pivot - 1
            if elem < target:
                start = pivot + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        results = []
        for elem in matrix:
            results.append(self.bsearch(elem, target))
        return any(results)
            
