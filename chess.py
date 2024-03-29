#Cat Jones and Skye Smith 

#Skye Smith
from pieces import rook, bishop, queen, king, knight, pawn

#Cat Jones
INIT_BOARD = [[rook.Rook("black",0,0), knight.Knight("black",0,1), bishop.Bishop("black",0,2), queen.Queen("black",0,3), king.King("black",0,4), bishop.Bishop("black",0,5), knight.Knight("black",0,6), rook.Rook("black",0,7)],
              [pawn.Pawn("black",1,0), pawn.Pawn("black",1,1), pawn.Pawn("black",1,2), pawn.Pawn("black",1,3), pawn.Pawn("black",1,4), pawn.Pawn("black",1,5), pawn.Pawn("black",1,6), pawn.Pawn("black",1,7)],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [pawn.Pawn("white",6,0), pawn.Pawn("white",6,1), pawn.Pawn("white",6,2), pawn.Pawn("white",6,3), pawn.Pawn("white",6,4), pawn.Pawn("white",6,5), pawn.Pawn("white",6,6), pawn.Pawn("white",6,7)],
              [rook.Rook("white",7,0), knight.Knight("white",7,1), bishop.Bishop("white",7,2), queen.Queen("white",7,3), king.King("white",7,4), bishop.Bishop("white",7,5), knight.Knight("white",7,6), rook.Rook("white",7,7)]]

def main():

    board = [] + INIT_BOARD

    player_color = "white"

    #Start of the while loop, which continues under the condition that the king isn't in checkmate per the checkmate function.
    checkmate = False 
    while checkmate == False:   

        #Cat Jones
        print(f"Ahoy, it's your turn {player_color}!")

        print_board(board)

        #current coordinate
        raw_cord = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
        piece, row, col = current_position_validation(raw_cord, player_color, board)

        #new move
        new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
        row, col = new_move_validation(new_move, piece, board)

        piece.update(row, col, board)

        #end end end
        #Cat Jones
        if checkmate:
            print_board(board)
            #gives interactive opportunity to play again, restarting the simulation
            print(f"Game over! {player_color.upper()} player has captured the rival king! Thanks for playing Skye and Cat's chess simulation!")
            play_again = input("Would you like to play again? Y or N: ")
            while play_again.upper != "Y" and play_again.upper != "N":
                print("Slip of the keyboard? Try again.")
                play_again = input("Would you like to play again? Y or N: ")

            if play_again.upper() == "N":
                print("Ok, goodbye :)")
                quit

            if play_again.upper() == "Y":
                checkmate = False
                board = [] + INIT_BOARD
                player_color = "white"
        
        if player_color == "white":
            player_color = "black"
        else:
            player_color = "white"


#-----------------------------------------------------------------------------------------------------------------------------      
      
#Cat Jones
def captured(board, ):

    captured_white = 0
    captured_black = 0

    if self.color(new_move) == other.color():
        
        if board([x][y]).get_color == white:
            captured_black = captured_black + 1
    #cap_color undefined
    elif cap_color == 'W' or cap_color == 'w':
        captured_white = captured_white + 1

    print(f"Captured by White: {captured_black} | Captured by Black: {captured_white}")
    
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

def new_move_validation(input_cord, piece, board):
    all_valid = False

    new_move = input_cord

    while not all_valid:

        valid = True

        #add validation for making sure theres a comma
        if valid and not(len(new_move) == 3 and new_move[0].isnumeric() and new_move[2].isnumeric() and new_move[1] == ","):
            print("Whoops, please format your coordinates correctly (ex: #,#)!") 
            new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
            valid = False
        else:
            new_cord = new_move.split(',')
            new_row = int(new_cord[0])
            new_col = int(new_cord[1])

        if valid and (new_col < 0 or new_col > 7 or new_row < 0 or new_row > 7):
            valid = False
            print("Whoops! Keep the pieces on the board!")
            new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")

        if valid:
            #after asking for new move validate the move is possible for the piece they selected
            move_validate = piece.validate_move(new_row, new_col, board)
            if move_validate == False:
                valid = False
                print("That move is not valid for that piece, please try again.")
                new_move = input("Please enter the coordinates for the space you would like to move the selected piece to (ex: 1,6): ")
                #add validation for making sure theres a comma
            else:
                all_valid = True

    return new_row, new_col

def print_board(board):
    for row in range(8):
        for col in range(8):
            print(board[row][col], end=" ")
        print()

main()