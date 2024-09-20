class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for row in board:
            if not self.checkNine(row):
                return False

        # check columns
        for x in range(len(board)):
            column = [board[0][x], board[1][x], board[2][x], 
                board[3][x], board[4][x], board[5][x], 
                board[6][x], board[7][x], board[8][x]]
            if not self.checkNine(column):
                return False

        # Check squares
        columnMarker = 0
        rowMarker = 0
        for i in range(len(board)):
            
            square = [board[rowMarker][columnMarker], 
                board[rowMarker][columnMarker + 1], 
                board[rowMarker][columnMarker+ 2], 
                board[rowMarker + 1][columnMarker], 
                board[rowMarker + 1][columnMarker + 1], 
                board[rowMarker + 1][columnMarker + 2], 
                board[rowMarker + 2][columnMarker], 
                board[rowMarker + 2][columnMarker + 1], 
                board[rowMarker + 2][columnMarker + 2], ]
            if not self.checkNine(square):
                return False

            columnMarker += 3
            if (columnMarker % 9 == 0):
                columnMarker = 0
                rowMarker += 3

        return True

    def checkNine(self, list: List[str]) -> bool:
        map = []
        for x in range(len(list)):
            if list[x] == '.':
                continue
            if list[x] in map:
                return False;

            map.append(list[x])

        return True