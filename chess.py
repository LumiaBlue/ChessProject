#Cat Jones

from pieces import rook, bishop, queen, king, knight, pawn

def main():        

    print("ahoy there matey, it's your turn!")

    #current coordinate
    piece = input("Please enter in the current coordinates of the piece you would like to place in play (ex: 2,4): ")
    #this splits the inputted coordinates by the comma, which is there for user visual-convience
    (col,row) = piece.split(',')

    #DO WORK YOU PAID FOR THIS TRAUMA
    #after asking for new move
    board[row][col].validate_move(new_row, new_col, board)



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

        
    #--------



    #Cat Jones
    captured_white = 0
    captured_black = 0
    #in the main file 
    #other.color????????
    if self.color(new_coor) == other.color(cur_coor):
        # if board([x][y]).get_color == white
        captured_black = captured_black + 1
        #cap_color undefined
    elif cap_color == 'W' or cap_color == 'w':
        captured_white = captured_white + 1

    print(f"Captured by White:{captured_black} | Captured by Black:{captured_white}")
    #--------

