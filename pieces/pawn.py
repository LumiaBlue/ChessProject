#Skye Smith
#class for Pawn pieces

class Pawn:
    #params: color - string; row - int; col - int
    #initialize an object of class Pawn
    #returns: none
    def __init__(self, color, row, col):
        self.type = "pawn"
        self.has_moved = False
        self.color = color
        self.row = row
        self.col = col

    #params: new_row - int; new_col - int; board - 2D list
    #check whether or not a given move is valid, considering the piece's current position as the origin point
    #returns: valid- boolean
    def validate_move(self, new_row, new_col, board):
        valid = True

        #initialize add, 
        add = 0
        if self.color == "white":
            add = -1
        else:
            add = 1

        if new_row == self.row and new_col == self.col:
            valid = False
        
        #validate a capture (diagonal move)
        if new_col != self.col:
            #is new_col equivalent to self.col + or - 1
            if abs(new_col - self.col) != 1:
                valid = False
            #is change in row != to 1 or in the wrong direction
            elif self.row + add != new_row:
                valid = False
            #is there no piece in the target destination
            elif board[new_row][new_col] == 0:
                valid = False 
            #is the piece in the target destination of the same color
            elif board[new_row][new_col].get_color == self.color:
                valid = False
        #first move double step
        elif abs(new_row - self.row) == 2:
            #is the move in the correct direction?
            if self.row + (2 * add) != new_row:
                valid = False
            #has the pawn moved previously?
            elif self.has_moved:
                valid = False
        #is the move not one space towards the opposite color edge of the board?
        elif self.row + add != new_row:
            vaid = False
        
        return valid
        
    #params: new_row - int; new_col - int; board - 2D list
    #update the object values for row and column, and "move" piece from former position to new position in board and change has_moved to True
    #returns: none 
    def update(self, new_row, new_col, board):
        self.has_moved = True
        board[new_row][new_col] = self
        board[self.row][self.col] = 0
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
        piece_type = "P"
        return color + piece_type