#Cat Jones
#class for Knight piece

class Knight:
    def _init_(self, color, row, col):
        self.type = "knight"
        self.color = color
        self.row = row
        self.col = col

    #is the move valid given the current position of the knight?
    def validate_move(self, new_row, new_col, board):

        valid = True 
        #staying in the same spot is not a valid 'move'
        if self.row == new_row and self.col == new_col:
            valid = False

        #given the 'L' shape, neither value can equal 0
        elif abs(new_col - self.col) < 1 or abs(new_row - self.row) < 1:
            valid = False
        #given the 'L' shape, neither value can be more than 2 
        elif abs(new_col - self.col) > 2 or abs(new_row - self.row) > 2:
            valid = False
            
        #given the 'L' shape, it's not valid for both values to equal 1
        elif abs(new_col - self.col) == 1 and abs(new_row - self.row) == 1:
            valid = False
        #given the 'L' shape, it's not valid for both value to equal 2
        elif abs(new_col - self.col) == 2 and abs(new_row - self.row) == 2:
            valid = False

        #is target position occupied by same-color piece
        if board[new_row][new_col] != 0 and board[new_row][new_col].get_color() == self.color:
            valid = False
        return valid                                    
    
    #otherwise named "def actually_move():"
    def update(self, new_row, new_col, board):
        board[new_row][new_col] = self
        self.row = new_row
        self.col = new_col
    
    #get color for processing information
    def get_color(self):
        return self.color
    
    #what type of piece is it?
    def get_type(self):
        return self.type