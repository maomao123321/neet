class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize haseset for row col and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for i in range(len(rows)):
            for j in range(len(cols)):
                val = board[i][j]
                if val == '.':
                    continue
                box_idx = (i // 3) * 3 + (j // 3)   # !!!

                if val in rows[i] or val in cols[j] or val in boxs[box_idx]:
                    return False
                
                # 往对应的 set 里加元素，用 add，不是 append
                rows[i].add(val)
                cols[j].add(val)
                boxs[box_idx].add(val)
        return True
            
