class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        col_cache = defaultdict(set)
        for i in range(9):
            row_cache = {}
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    #box check
                    br, bc = i//3,j//3
                    box_key = (br,bc)
                    if val in boxes[box_key]:
                        return False
                    boxes[box_key].add(val)

                    #row check
                    if val in row_cache:
                        return False
                    row_cache[val] = j

                    if val in col_cache[j]:
                        return False
                    col_cache[j].add(val)

        return True
