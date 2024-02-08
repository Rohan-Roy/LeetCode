"""
### Problem

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""
### Solution

class Solution(object):
    boardSize = 10
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            print(board[i][:])
        
        
        
        flagRow, flagCol, flagSub = set(), set(), set()
        for i in range(9):
            flagRow.clear()
            flagCol.clear()
            flagSub.clear()
            for j in range(9):
                if board[i][j] >= '0' and board[i][j] <= '9':
                    if board[i][j] in flagRow:
                        return False
                    flagRow.add(board[i][j])
                
                if board[j][i] >= '0' and board[j][i] <= '9':
                    if board[j][i] in flagCol:
                        return False
                    flagCol.add(board[j][i])
                
                r = 3* (i // 3) + j // 3
                c = 3 * (i % 3) + j % 3
                if board[r][c] >= '0' and board[r][c] <= '9':
                    if board[r][c] in flagSub:
                        return False
                    flagSub.add(board[r][c])
        return True
    

solution = Solution()
board =   [ [ '5', '3', '.', '.', '7', '.', '.', '.', '.' ],
            [ '6', '.', '.', '1', '9', '5', '.', '.', '.' ],
            [ '.', '9', '8', '.', '.', '.', '.', '6', '.' ],
            [ '8', '.', '.', '.', '6', '.', '.', '.', '3' ],
            [ '4', '.', '.', '8', '.', '3', '.', '.', '1' ],
            [ '7', '.', '.', '.', '2', '.', '.', '.', '6' ],
            [ '.', '6', '.', '.', '.', '.', '2', '8', '.' ],
            [ '.', '.', '.', '4', '1', '9', '.', '.', '5' ],
            [ '.', '.', '.', '.', '8', '.', '.', '7', '9' ] ]
print(solution.isValidSudoku(board))