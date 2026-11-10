class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        check_row = collections.defaultdict(set)
        check_col = collections.defaultdict(set)
        check_box = collections.defaultdict(set)

        for i in range(row):
            for j in range((col)):
                val = board[i][j]
                if val == '.':
                    continue
                box_key = (i//3,j//3)
                if (val in check_row[i] or val in check_col[j] or val in check_box[box_key]):
                    return False
                check_row[i].add(val)
                check_col[j].add(val)
                check_box[box_key].add(val)
        return True