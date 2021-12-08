#Cat Jones
#class for King piece

class King:
    def _init_(self, color, row, col):
        self.type = "king"
        self.color = color
        self.row = row
        self.col = col

    def validate_move(self, new_row, new_col, board):
        valid = True 

        #staying in the same spot is not a valid 'move'
        if self.row == new_row and self.col == new_col:
            valid = False

        #difference one or zero (can't both be zero)        
        elif abs(new_col - self.col) > 1 or abs(new_row - self.row) > 1:
                valid = False

        #is target position occupied by same-color piece?
        if board[new_row][new_col] != 0 and board[new_row][new_col].get_color() == self.color:
            valid = False

        return valid
                                    
    def update(self, new_row, new_col, board):
        board[new_row][new_col] = self
        self.row = new_row
        self.col = new_col
    
    def get_color(self):
        return self.color
    
    def get_type(self):
        return self.type

    #getting the king's new coordinates for check/checkmate functions
    def get_col(self):
        return self.col

    #getting the king's new coordinates for check/checkmate functions
    def get_row(self):
        return self.row
    
    def check(row, col, board):
        