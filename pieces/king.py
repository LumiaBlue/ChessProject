#Cat Jones
#class for King piece

class King:
    #params: color - string; row - int; col - int
    #initialize an object of class King
    #returns: king object
    def __init__(self, color, row, col):
        self.type = "king"
        self.color = color
        self.row = row
        self.col = col

    #params: new_row - int; new_col - int; board - 2D list
    #check whether or not a given move is valid, considering the piece's current position as the origin point
    #returns: valid- boolean
    def validate_move(self, new_row, new_col, board):
        valid = True 
        if self.row == new_row and self.col == new_col:
            valid = False

        elif abs(new_col - self.col) > 1 or abs(new_row - self.row) > 1:
                valid = False
                #difference one or zero (can't both be zero)
        
        elif self.check(new_row, new_col, board):
            valid = False

        #Is target position occupied by same-color piece
        if board[new_row][new_col] != 0 and board[new_row][new_col].get_color() == self.color:
            valid = False

        return valid

    #params: new_row - int; new_col - int; board - 2D list
    #update the object values for row and column, and "move" piece from former position to new position in board and change has_moved to True
    #returns: none                      
    def update(self, new_row, new_col, board):
        board[self.row][self.col] = 0
        board[new_row][new_col] = self

        #update ninth row of chess board
        if self.color() == "white":
            board[9][2] = new_row
            board[9][3] = new_col
        else:
            board[9][0] = new_row
            board[9][1] = new_col

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

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row
    
    #params: none
    #string conversion of the object, represent color and type
    #returns string
    def __str__(self):
        color = self.color[0]
        piece_type = "K"
        return color + piece_type
    
    #Skye Smith
    #params: row - int; col - int; board - 2D-list
    #determines whether or not a king of this object's color would be in check at the given position on the given board
    #returns: check - boolean
    def check(self, row, col, board):
        check = False
        
        #row and column checks (Rook and Queen)
        #check for vertical sightline below king
        for i in range(row + 1, 8):
            piece = board[i][col]
            if piece != 0:
                if piece.get_color() != self.color and (piece.get_type() == "rook" or piece.get_type() == "queen"):
                    check = True
                #end loop on first sighted piece, piece of same color/wrong type will still obscure line of attack
                break
        
        #check for vertical sightline above king
        if not(check):
            for i in range(row - 1, -1, -1):
                piece = board[i][col]
                if piece != 0:
                    if piece.get_color() != self.color and (piece.get_type() == "rook" or piece.get_type() == "queen"):
                        check = True
                    #end loop on first sighted piece, piece of same color/wrong type will still obscure line of attack
                    break

        #check horizontal sightline to the right
        if not(check):
            for i in range(col + 1, 8):
                piece = board[row][i]
                if piece != 0:
                    if piece.get_color() != self.color and (piece.get_type() == "rook" or piece.get_type() == "queen"):
                        check = True
                    #end loop on first sighted piece, piece of same color/wrong type will still obscure line of attack
                    break

        #check for horizontal sightline to the left
        if not(check):
            for i in range(col - 1, -1, -1):
                piece = board[row][i]
                if piece != 0:
                    if piece.get_color() != self.color and (piece.get_type() == "rook" or piece.get_type() == "queen"):
                        check = True
                    #end loop on first sighted piece, piece of same color/wrong type will still obscure line of attack
                    break
        
        #diagonal line checks (Bishop and Queen)
        for row_add in [-1, 1]:
            #skips rest of the diagonal checks if king is already in check
            if check:
                break
            for col_add in [-1, 1]:
                #skips second cycle of loop if king is in check
                if check:
                    break
                temp_row = row + row_add
                temp_col = col + col_add
                while temp_row <= 7 and temp_row >= 0 and temp_col <= 7 and temp_col >= 0:
                    piece = board[temp_row][temp_col]
                    if piece != 0:
                        if piece.get_color() != self.color and (piece.get_type() == "bishop" or piece.get_type() == "queen"):
                            check = True
                        #if there is a piece, it will either place king in check, or obscure the line of attack from any pieces beyond it
                        break
                        
                    temp_row += row_add
                    temp_col += col_add
        
        #L checks (Knight)
        if not(check):
            for d_row in [-2, -1, 1, 2]:
                for d_col in [-2, -1, 1, 2]:
                    knight_row = row + d_row
                    knight_col = col + d_col
                    if d_col != d_row and not(knight_row > 7 or knight_row < 0 or knight_col > 7 or knight_col < 0):
                        piece = board[row + d_row][col + d_col]
                        if piece != 0 and piece.get_type() == "knight" and piece.get_color() != self.color:
                            check = True
                            #break only if put in check, knights jump and line of attack can't be obscure
                            break
        
        #pawn checks
        #initialize add, which direction does a pawn need to be in to threaten the king
        if not(check):
            add = 0
            if self.color == "white":
                add = -1
            else:
                add = 1
            for i in [-1, 1]:
                piece = board[row + add][col + i]
                if piece != 0:
                    if piece.get_type() == "pawn" and piece.get_color() != self.color:
                        check = True
                        #saves checking second space if first space is aggressing pawn, but doesn't skip second space if not
                        break
        
        return check