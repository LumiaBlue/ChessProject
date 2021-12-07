#Cat Jones
#class for Queen pieces

class Knight:
    def _init_(self, color, row, col):
        self.type = "knight"
        self.color = color
        self.row = row
        self.col = col

    def validate_move(self, new_row, new_col, board):
                                    

    def update(self, new_row, new_col, board):
        board[new_row][new_col] = self
        self.row = new_row
        self.col = new_col
    
    def get_color(self):
        return self.color
    
    def get_type(self):
        return self.type