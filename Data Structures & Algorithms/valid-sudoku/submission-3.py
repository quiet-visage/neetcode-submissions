from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check duplicates in blocks
        for ri in range(0, 9, 3):
            for ci in range(0, 9, 3):
                block_piece = [
                    item
                    for row in board[ri : ri + 3]
                    for item in row[ci : ci + 3]
                ]
                nums = [x for x in block_piece if x != "."]
                has_duplicates = len({*nums}) != len(nums)
                if has_duplicates: 
                    return False

        for i in range(9):
            col_cache = {}
            row_cache = {}
            for j in range(9):
                row_val = board[i][j]
                if row_val != '.' and row_val in row_cache:
                    return False
                row_cache[row_val] = j

                col_val = board[j][i]
                if col_val != '.' and col_val in col_cache:
                    return False
                col_cache[col_val] = j
        return True
