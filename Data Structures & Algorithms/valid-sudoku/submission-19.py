class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        col_cache = defaultdict(set)
        for i in range(9):
            row_cache = {}
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                box_key = (i//3,j//3)
                if val in boxes[box_key]:
                    return False
                boxes[box_key].add(val)

                if val in row_cache:
                    return False
                row_cache[val] = j

                if val in col_cache[j]:
                    return False
                col_cache[j].add(val)

        return True
