#Skye Smith
#class for bishop pieces

class Rook:
    def _init_(self, color, row, col):
        self.type = "bishop"
        self.color = color
        self.row = row
        self.col = col

    def validate_move(self, new_row, new_col, board):
        valid = True

        dist = abs(new_col - self.col)
        if dist != abs(new_row - self.row):
            valid = False
        elif 



        
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