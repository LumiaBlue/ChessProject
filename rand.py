#--------
cur_coor = (self.col,self.row)
#current coordinate

print("it's your turn!")
new_col = input("Enter the x-coordinate for your next move: )
new_row = input("Enter the y-coordinate for your next move: )

new_coor = (new_col,new_row)

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



#--------
captured_white = 0
captured_black = 0

#other.color????????
if self.color(new_coor) == other.color(cur_coor):
    #captured color
    cap_color = input("What color is the piece that was captured? B or W: ")
    if cap_color != 'B' and cap_color != 'b' and cap_color != 'W' and cap_color != 'w':
        print("Please select a valid piece color.")
        cap_color = input("What color is the piece that was captured? B or W: ")
    elif cap_color == 'B' or cap_color == 'b':
        captured_black = captured_black + 1
    elif cap_color == 'W' or cap_color == 'w':
        captured_white = captured_white + 1

print(f"{}")
#--------
