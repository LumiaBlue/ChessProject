#Cat Jones
#class for Queen pieces

class King:
    def _init_(self, color, row, col):
        self.type = "king"
        self.color = color
        self.row = row
        self.col = col

    def validate_move(self, new_row, new_col, board):
        valid = True 
        if self.row == new_row and self.col == new_col:
            valid = False
        elif self.row == new_row:
            for i in range (self.row, new_row):
                if


            #difference one or zero (can't both be zero)
        elif self.col == new_col:
            for i in range (self.col, new_col):
                if 
            #difference one or zero (can't both be zero)

        else:
            valid = False

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

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row