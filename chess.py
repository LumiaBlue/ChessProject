#Cat Jones and Skye Smith 

#Skye Smith
from pieces import rook, bishop, queen, king, knight, pawn
import copy

#Cat Jones
INIT_BOARD = [[rook.Rook("black",0,0), knight.Knight("black",0,1), bishop.Bishop("black",0,2), queen.Queen("black",0,3), king.King("black",0,4), bishop.Bishop("black",0,5), knight.Knight("black",0,6), rook.Rook("black",0,7)],
              [pawn.Pawn("black",1,0), pawn.Pawn("black",1,1), pawn.Pawn("black",1,2), pawn.Pawn("black",1,3), pawn.Pawn("black",1,4), pawn.Pawn("black",1,5), pawn.Pawn("black",1,6), pawn.Pawn("black",1,7)],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [pawn.Pawn("white",6,0), pawn.Pawn("white",6,1), pawn.Pawn("white",6,2), pawn.Pawn("white",6,3), pawn.Pawn("white",6,4), pawn.Pawn("white",6,5), pawn.Pawn("white",6,6), pawn.Pawn("white",6,7)],
              [rook.Rook("white",7,0), knight.Knight("white",7,1), bishop.Bishop("white",7,2), queen.Queen("white",7,3), king.King("white",7,4), bishop.Bishop("white",7,5), knight.Knight("white",7,6), rook.Rook("white",7,7)],
              #extra row to store coordinates of kings
              #black_row, black_col, white_row, white_col
              [0, 4, 7, 4]]

#Cat Jones
def main():

    board = copy.deepcopy(INIT_BOARD)

    player_color = "white"

    captured_white = 0
    captured_black = 0
    king_row = 7
    king_col = 4

    #Start of the while loop, which continues under the condition that the king isn't in checkmate per the checkmate function.
    checkmate = False 
    while checkmate == False:   
        print(f"Ahoy, it's your turn {player_color.upper()}!")

        #print current board to console
        print_board(board, captured_black, captured_white)

        #user turn
        valid = False
        while not(valid):
            #current coordinate
            raw_cord = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
            piece, cur_row, cur_col = current_position_validation(raw_cord, player_color, board)
            #new move
            new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
            valid, row, col = new_move_validation(new_move, piece, board)

            #determine if king is in check after move
            if valid:
                #copy the current board
                temp_board = copy_board(board)

                #"move" the piece
                #avoids .update, leaving pawn's has_moved variable unchanged 
                temp_board[row][col] = piece
                temp_board[cur_row][cur_col] = 0

                #assign king to the current player's king and check if it is in check with this move
                if player_color == "black":
                    #get cords of black king
                    king_row = board[8][0]
                    king_col = board[8][1]
                else:
                    #get cords of white king
                    king_row = board[8][2]
                    king_col = board[8][3]

                king = board[king_row][king_col]
                if king.check(king_row, king_col, temp_board):
                    print("Whoa there, that move places/leaves your king in check!")
                    concede = validate_concession()
                    if concede:
                        valid = True
                        row = cur_row
                        col = cur_row
                        checkmate = True
                    else:
                        valid = False

        #checks if an opposing piece is captured with the execution of the new move
        capture_piece = captured(board, row, col)
        if capture_piece == True:
            if player_color == "white":
                captured_black += 1
            if player_color == "black":
                captured_white += 1

        #move piece and update the board list
        piece.update(row, col, board)

        #switch active player
        if player_color == "white":
            player_color = "black"
        else:
            player_color = "white"

        #end end end
        #Cat Jones
        if checkmate:
            print_board(board, captured_black, captured_white)
            #gives interactive opportunity to play again, restarting the simulation
            print(f"Game over! {player_color.upper()} player has captured the rival king! Thanks for playing Skye and Cat's chess simulation!")
            play_again = input("Would you like to play again? Y or N: ")

            #validate user input
            while play_again.upper() != "Y" and play_again.upper() != "N":
                print("Slip of the keyboard? Try again.")
                play_again = input("Would you like to play again? Y or N: ")

            #exit game if user doesn't want to play again
            if play_again.upper() == "N":
                print("Ok, goodbye :)")
                quit
            
            #reset to initial conditions
            if play_again.upper() == "Y":
                checkmate = False
                board = copy.deepcopy(INIT_BOARD)
                player_color = "white"
                captured_white = 0
                captured_black = 0


#-----------------------------------------------------------------------------------------------------------------------------      
      
#Cat Jones
#params: baord - 2d list; row - int; col - int
#determines whether or not there is a piece at the given coordinates on the given board
#return: captured - boolean
def captured(board, row, col):

    captured = False

    if board[row][col] != 0:
        captured = True

    return captured

#Cat Jones
#params: input_cord - str; player_color - str; board - 2D list
#accepts an initial string representating coordinates of the piece the player wants to select and validates this input, 
#returning the selected piece, and the coordinates of that piece
#return: piece - chess piece; row - int; col - int
def current_position_validation(input_cord, player_color, board):
    piece = 0
    all_valid = False

    raw_cord = input_cord

    #validate all of the weird things
    #current position
    while not all_valid:

        valid = True

        #add validation for making sure format is correct
        if not(len(raw_cord) == 3 and raw_cord[0].isnumeric() and raw_cord[2].isnumeric() and raw_cord[1] == ","):
            print("Whoops, please format your coordinates correctly (ex: #,#)!")
            raw_cord = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
            #this splits the inputted coordinates by the comma, which is there for user visual-convience
            valid = False
        else:
            cord = raw_cord.split(',')
            row = int(cord[0])
            col = int(cord[1])

        #validation that the piece they wish to play is actually on the board
        if valid and (col < 0 or col > 7 or row < 0 or row > 7):
            valid = False
            print("Whoops! Eyes on the board!")
            raw_cord = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")

        #if the value == 0, empty space bad
        if valid and board[row][col] == 0:
            valid = False
            print("Please select a piece to put in play.")
            raw_cord = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
        elif valid:
            piece = board[row][col]

        if valid and piece.get_color() != player_color:
            valid = False
            print("Unfair advantage! Play one of your own pieces please.")
            raw_cord = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
        
        if valid:
            all_valid = True

    return piece, row, col

#Cat Jones
#params: input_cord - str; piece - object (one of chess pieces); board - 2D list
#accepts an initial string of user input representing destination coordinates, and validates that input with the given piece and board and converts it into integer values
#return: valid - boolean; new_row - int, new_col - int
def new_move_validation(input_cord, piece, board):
    new_move = input_cord

    valid = True
    new_row = 0
    new_col = 0

    #add validation for making sure theres a comma
    if valid and not(len(new_move) == 3 and new_move[0].isnumeric() and new_move[2].isnumeric() and new_move[1] == ","):
        print("Whoops, please format your coordinates correctly (ex: #,#)!") 
        valid = False
    else:
        new_cord = new_move.split(',')
        new_row = int(new_cord[0])
        new_col = int(new_cord[1])

    if valid and (new_col < 0 or new_col > 7 or new_row < 0 or new_row > 7):
        valid = False
        print("Whoops! Keep the pieces on the board!")

    if valid:
        #after asking for new move validate the move is possible for the piece they selected
        move_validate = piece.validate_move(new_row, new_col, board)
        if move_validate == False:
            valid = False
            print("That move is not valid for that piece, please try again.")

    return valid, new_row, new_col

#Skye Smith
#params: board - 2D list; captured_black - int; captured_white - int
#prints out the given board
#return: none
def print_board(board, captured_black, captured_white):
    print("  0   1   2   3   4   5   6   7")
    for row in range(8):
        print(f"{row} ", end="")
        for col in range(8):
            piece = str(board[row][col])
            print(f"{piece:4}", end="")
        print()
    print(f"Captured by White: {captured_black} | Captured by Black: {captured_white}")

#Skye Smith
#params: board - 2D list
#creates a copy of the entered board
#return: copy - 2D list
def copy_board(board):
    copy = []
    for row in board:
        copy.append([] + row)
    
    return copy

#Skye Smith
#params: none
#queries the user to determine if they are in checkmate
#return: end - boolean
def validate_concession():
    concede = input("Are you in checkmate? Y or N: ")
    end = False

    #validate user input
    while concede.lower() != "y" and concede.lower() != "n":
        print("Slip of the keyboard? Try again.")
        concede = input("Are you in checkmate? Y or N: ")

    #return true if the user enters Y
    if concede.lower() == "y":
        end = True

    return end

main()