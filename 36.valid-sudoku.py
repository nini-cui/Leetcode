#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
from typing import List
# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # no of rows
        no_rows = len(board)
        no_cols = len(board[0])
        for i in range(no_rows):
            res = []
            for j in range(no_cols):
                if board[i][j] != '.':
                    int_val = int(board[i][j])
                    if int_val > 9:
                        return False
                    res.append(int_val)

            if len(res) != len(set(res)):
                return False
            
        for i in range(no_cols):
            res = []
            for j in range(no_rows):
                if board[j][i] != '.':
                    int_val = int(board[j][i])
                    if int_val > 9:
                        return False
                    res.append(int_val)

            if len(res) != len(set(res)):
                return False
            
        for i in range(0, 9, 3):
            
# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    solution.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
