from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        # check duplicates in blocks
        for ri in range(0, n, 3):
            for ci in range(0, n, 3):
                idx = (ri / 3) * 3 + (ci / 3)
                block_piece = [
                    item
                    for row in board[ri : ri + 3]
                    for item in row[ci : ci + 3]
                ]
                nums = [x for x in block_piece if x != "."]
                has_duplicates = len({*nums}) != len(nums)
                if has_duplicates: 
                    return False

        # check duplicates in rows
        for row in board:
            cache = {}
            for i in range(9):
                if row[i] == ".": 
                    continue

                if row[i] in cache:
                    return False

                cache[row[i]] = i


        # check duplicates in cols
        ls = defaultdict(list)
        for i in range(9):
            cache = {}
            for j in range(9):
                column = board[j][i]
                if column != '.' and column in cache:
                    return False
                cache[column] = j
        return True
