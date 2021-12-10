#Skye Smith
#class for Rook pieces

class Rook:
    #params: color - string; row - int; col - int
    #initialize an object of class Rook
    #returns: none
    def __init__(self, color, row, col):
        self.type = "rook"
        self.color = color
        self.row = row
        self.col = col

    #params: new_row - int; new_col - int; board - 2D list
    #check whether or not a given move is valid, considering the piece's current position as the origin point
    #returns: valid- boolean
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
            for i in range(self.col + add, new_col, add):
                #check occupancy
                if board[self.row][i] != 0:
                    valid = False
                    break
        #check occupancy for vertical move
        elif self.col == new_col:
            #increment through rows between current and target positions
            for i in range(self.row + add, new_row, add):
                #check occupancy
                if board[i][new_col] != 0:
                    valid = False
                    break
        #is move not horizontal or vertical
        else:
            valid = False
        
        #Is target position occupied by same-color piece
        if board[new_row][new_col] != 0 and board[new_row][new_col].get_color() == self.color:
            valid = False
        
        return valid
                            
    #params: new_row - int; new_col - int; board - 2D list
    #update the object values for row and column, and "move" piece from former position to new position in board
    #returns: none 
    def update(self, new_row, new_col, board):
        board[self.row][self.col] = 0
        board[new_row][new_col] = self
        
        self.row = new_row
        self.col = new_col
    
    #params: none
    #return the current value of an object's color variable
    #returns: self.color - string
    def get_color(self):
        return self.color
    
    #params: none
    #returns the current value of an object's type variable
    #returns: self.type - string
    def get_type(self):
        return self.type
    
    #params: none
    #string conversion of the object, represent color and type
    #returns string
    def __str__(self):
        color = self.color[0]
        piece_type = "R"
        return color + piece_type