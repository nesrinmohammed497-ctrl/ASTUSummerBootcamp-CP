class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        r=len(board)
        for i in range(r):
            row=[]
            col=[]
            for j in range(r):
                
                if board[i][j] != ".":
                    if  board[i][j] in row:
                        return False
                    row.append (board[i][j])
                if board[j][i] != ".":
                    if  board[j][i] in col:
                        return False
                    col.append (board[j][i])
                print col
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = []
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        if board[i][j] != '.':
                            if board[i][j] in seen:
                                return False
                            seen.append(board[i][j])
        return True
                

        