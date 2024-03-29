#Skye Smith
#class for Queen pieces

class Queen:
    #params: color - string; row - int; col - int
    #initialize an object of class Queen
    #returns: none
    def __init__(self, color, row, col):
        self.type = "queen"
        self.color = color
        self.row = row
        self.col = col

    #params: new_row - int; new_col - int; board - 2D list
    #check whether or not a given move is valid, considering the piece's current position as the origin point
    #returns: valid- boolean
    def validate_move(self, new_row, new_col, board):
        valid = True

        #is the target row greater than the current row?
        #establish add_row to help step through spaces between current pos and target pos
        add_row = 0
        if new_row > self.row:
            add_row = 1
        else:
            add_row = -1

        #is the target col greater than the current row?
        #establish add_col to help step through spaces between current pos and target pos
        add_col = 0
        if new_col > self.col:
            add_col = 1
        else:
            add_col = -1

        #is target position the same as current position?
        if self.row == new_row and self.col == new_col:
            valid = False

        #is move horizontal, vertical or diagonal?
        dist = abs(new_col - self.col)
        diagonal = dist == abs(new_row - self.row)
        horizontal = self.row == new_row and self.col != new_col
        vertical = self.col == new_col and self.row != new_row
        if not(diagonal or vertical or horizontal):
            valid = False
        
        #check occpancy in spaces between current and target position
        if diagonal:
            #Are there any pieces in the path to the target position?
            #use loop to step through spaces between current and target positions
            temp_col = self.col
            #add + or - 1 (add_row) to self.row so that the current position is not checked for occupancy
            for i in range(self.row + add_row, new_row,add_row):
                #increment temp_col towards new_col
                temp_col += add_col
                if board[i][temp_col] != 0:
                    valid = False
        elif horizontal:
            #increment through columns between current and target positions
            for i in range(self.col + add_col, new_col, add_col):
                #check occupancy
                if board[self.row][i] != 0:
                    valid = False
        elif vertical:
            #increment through rows between current and target positions
            for i in range(self.row + add_row, new_row, add_row):
                #check occupancy
                if board[i][new_col] != 0:
                    valid = False
                    break      
        
        #is there a same-color piece at the target position?
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
        piece_type = "Q"
        return color + piece_type