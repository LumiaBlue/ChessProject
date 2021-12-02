#Skye Smith
#class for rook pieces

class Rook:
    def _init_(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def validate_move(self, new_row, new_col, board):
        valid = True
        if self.row == new_row and self.col == new_col:
            valid = False
        elif self.row == new_row:
            for i in range(self.col, new_col):
                if board[self.row][i] != 0:
                    valid = False
                    break
        elif self.col == new_col:
            for i in range(self.row, new_row):
                if board[i][new_col] != 0:
                    valid = False
                    break
        else:
            valid = False
        
        if board[new_row][new_col] != 0 and board[new_row][new_col].get_color() == self.color:
            valid = False
        
        return valid
                            

    def update(self, new_row, new_col, board):
            board[new_row][new_col] = self
            self.row = new_row
            self.col = new_col