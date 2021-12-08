#Cat Jones and Skye Smith 

#Skye Smith
from pieces import rook, bishop, queen, king, knight, pawn

def main():

    #Cat Jones
    board = [[rook.Rook("black",0,0), knight.Knight("black",0,1), bishop.Bishop("black",0,2), queen.Queen("black",0,3), king.King("black",0,4), bishop.Bishop("black",0,5), knight.Knight("black",0,6), rook.Rook("black",0,7)],
            [pawn.Pawn("black",1,0), pawn.Pawn("black",1,1), pawn.Pawn("black",1,2), pawn.Pawn("black",1,3), pawn.Pawn("black",1,4), pawn.Pawn("black",1,5), pawn.Pawn("black",1,6), pawn.Pawn("black",1,7)],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [pawn.Pawn("white",6,0), pawn.Pawn("white",6,1), pawn.Pawn("white",6,2), pawn.Pawn("white",6,3), pawn.Pawn("white",6,4), pawn.Pawn("white",6,5), pawn.Pawn("white",6,6), pawn.Pawn("white",6,7)],
            [rook.Rook("white",7,0), knight.Knight("white",7,1), bishop.Bishop("white",7,2), queen.Queen("white",7,3), king.King("white",7,4), bishop.Bishop("white",7,5), knight.Knight("white",7,6), rook.Rook("white",7,7)]]

    #Start of the while loop, which continues under the condition that the king isn't in checkmate per the checkmate function.
    checkmate = False 
    while checkmate = False:   

        #Cat Jones
        print("ahoy, it's your turn!")

        #current coordinate
        piece = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
        #add validation for making sure theres a comma
        if "," not in piece:
            print("Whoops, please include a comma between your coordinates!")
            piece = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
        #this splits the inputted coordinates by the comma, which is there for user visual-convience
        (col,row) = piece.split(',')

        #!!!!!!!if the value == 0, empty space bad!!!!!!
        if board[row][col] == 0:
            valid = False
            print("Please select a piece to put in play.")
            piece = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
            (col,row) = piece.split(',')

        #validation that the piece they wish to play is actually on the board
        if col < 0 or col > 7 or row < 0 or col > 7:
            valid = False
            print("Whoops! Eyes on the board!")
            piece = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
            (col,row) = piece.split(',')

        new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
        #add validation for making sure theres a comma
        if "," not in new_move:
            print("Whoops, please include a comma between your coordinates!")
            new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
        (new_col,new_row) = new_move.split(',')

        if new_col < 0 or new_col > 7 or new_row < 0 or new_col > 7:
            valid = False
            print("Whoops! Keep the pieces on the board!")
            new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
            (new_col,new_row) = new_move.split(',')

        #after asking for new move validate the move is possible for the piece they selected
        board[row][col].validate_move(new_row, new_col, board)

        while 

        #new coordinate
        new_coor = (new_col,new_row)



        #Cat Jones
        #this chunk is here for user convience, allowing them to rethink their move and change it if they wish
        confirm_move = input(f"Please confirm that you would like to move this piece to {new_coor} with a Y or N: ")
        if confirm_move != 'Y' and confirm_move != 'y' and confirm_move != 'N' and confirm_move != 'n':
            print("Please pick a valid option.")
            confirm_move = input(f"Please confirm that you would like to move this piece to {new_coor} with a Y or N: ")
        elif confirm_move == 'Y' or confirm_move == 'y':
            #proceed to move piece
        elif confirm_move == 'N' or confirm_move == 'n':
            new_col = input("Enter the x-coordinate for your next move: )
            new_row = input("Enter the y-coordinate for your next move: )

            new_coor = (new_col,new_row) 

            

    #Cat Jones
    def captured():

        captured_white = 0
        captured_black = 0

        #in the main file 
        if self.color(new_coor) == other.color(cur_coor):
            # if board([x][y]).get_color == white
            captured_black = captured_black + 1
            #cap_color undefined
        elif cap_color == 'W' or cap_color == 'w':
            captured_white = captured_white + 1

        print(f"Captured by White: {captured_black} | Captured by Black: {captured_white}")

