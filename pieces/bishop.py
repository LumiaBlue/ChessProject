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


        add_row = 0
        if new_row > self.row:
            add_row = 1
        else:
            add_row = -1

        add_col = 0
        if new_col > self.col:
            add_col = 1
        else:
            add_col = -1

        dist = abs(new_col - self.col)
        if dist != abs(new_row - self.row):
            valid = False
        
        temp_col = self.col
        for i in range(self.row + add_row, new_row):
            temp_col += add_col
            if board[temp_col][i] != 0:
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