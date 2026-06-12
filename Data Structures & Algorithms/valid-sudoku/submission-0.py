class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = []
        cols = []
        boxes = []

        for i in range(9):
            rows.insert(i, [])
            cols.insert(i, [])
            boxes.insert(i, [])

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                
                box_idx = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False
                
                rows[i].append(val)
                cols[j].append(val)
                boxes[box_idx].append(val)

        return True