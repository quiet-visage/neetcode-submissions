from pprint import pprint
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)
        for i in range(9):
            col_cache = {}
            row_cache = {}
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    br, bc = i//3,j//3
                    box_key = (br,bc)
                    if val in boxes[box_key]:
                        return False
                    boxes[box_key].add(val)

                row_val = board[i][j]
                if row_val != '.' and row_val in row_cache:
                    return False
                row_cache[row_val] = j

                col_val = board[j][i]
                if col_val != '.' and col_val in col_cache:
                    return False
                col_cache[col_val] = j
                
        pprint(boxes)

        return True
