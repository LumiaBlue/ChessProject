#Skye Smith
#class for rook pieces

class Rook:
    def _init_(self, color, row, col):
        self.type = "rook"
        self.color = color
        self.row = row
        self.col = col

    def validate_move(self, new_row, new_col, board):
        valid = True

        #establish "add" to allow non-inclusive steps through path between current and target positions
        add = 0
        if new_row > self.row or new_col > self.col:
            add = 1
        else:
            add = -1

        #is target position the same as current position?
        if self.row == new_row and self.col == new_col:
            valid = False
        #check occupancy for horizontal move
        elif self.row == new_row:
            #increment through columns between current and target positions
            for i in range(self.col + add, new_col):
                #check occupancy
                if board[self.row][i] != 0:
                    valid = False
                    break
        #check occupancy for vertical move
        elif self.col == new_col:
            #increment through rows between current and target positions
            for i in range(self.row + add, new_row):
                #check occupancy
                if board[i][new_col] != 0:
                    valid = False
                    break
        #is move not horizontal or vertical
        else:
            valid = False
        
        #Is target position occupied by smae-color piece
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