#**********************  Othello.py  *********************
#
# Name: Alexander Quirindongo
#
# Course: CSCI 1470
#
# Assignment: Othello Project
#
# Algorithm:
#   Assign various varibles for board_size, color pieces for each player, whose turn it is, tracking how many pieces a player has, and for later, checking a pieces surrounding area.
#   Create new functions to be handled in the main that creates the board, prints the board, determines whether a move is valid, making the move and for flipping the necessary pieces.
#   In the Create board function that calls in a board, create a new 8 x 8 list and use the format it provides as a "fake" gameboard. Append EM to each list except for the 4 middle squares which have 2 of both colors connected diagonally
#   In the Print Board function that calls in a board, create numbers across the top to line up with the list to act as a column numbers. In a loop, print out the board sent in. Print out the index variable to act as row numbers.
#   The horizontal lines function acts as a way to space out the list's "squares"
#   In the MakeMove function, simply place the piece of the player playing into the square they ask for. The out of bounds function acts as a guard against buffer overflow errors so that the player cannot play outside the specified game border.
#   The Valid Move function is where all the rules of reversi will take place. It checks to see if a player has chosen a legal square, whether the square is occupied, and then will go through a series of tests to see if the player can capture an opponent's piece.
#       First, it will check if the square chosen by the player has any piece surrounding it by using the surroundpiece list to check its surroundings. It will check to make sure that square is not out of bounds and whether it is occupied by an opponent's piece
#       If it finds an opponent's piece, We will continue in that direction using the same values given by the list. If that new square is not of bounds and is also occupied by an opponent's piece, we will have a loop to continue going in that direction
#           While the chosen square still contains an opponent's piece, continue to keep going until you find a square that is either empty or occupied by your own piece. Break out of the loop once this is achieved.
#       Outside that loop, check to see if that square is still within the boundaries and see if that square is occupied by your piece.
#       If it is, you are now able to capture pieces. In a loop, go backwards, flipping pieces along the way until you reach where the player initially placed their piece. Have a counter to tell the game that a piece was flipped.
#       Once it reaches the originally chosen square, break out of the loop and and verify that a piece was flipped. 
#       If a piece was flipped, allow the player to make his original move by sending in the original row and column the player chose. Place their new piece there using the MakeMove Function.
#   With all of those functions created and the rules laid out in the Valid Move function. You can proceed to create a game board for players to play on.
#   While a winner has not been decided, use the game board you created to print out a new board everytime a move was made whether legally or illegally.
#       In the while loop, keep track for the players how many pieces they both have, how many illegal moves were made, and whose turn it is.
#       Ask the current player's turn for their move and use the valid move function above to check to make sure they made a legal move.
#       Since we have not established a way to check whether a player can make a valid move or not, instead, skip a player's turn if they make 3 illegal moves.
#       That way, if they run into a siutation where they cannot capture an opponent's piece, their turn will eventually be skipped like it would normally in Reversi.
#       Everything else will still follow Reversi's original rules.
#       Once either a player loses all their pieces or all 64 pieces have been placed on the board, declare a winner by seeing who has the most points at the end.
#   Points are decided by the number of tiles they own.
#
#   Reference code was used for black and white circles. This is a unicode specifically for creating a medium white circle and a medium black circle.
#   This code was obtained from: https://www.charbase.com/26aa-unicode-medium-white-circle and https://www.charbase.com/26ab-unicode-medium-black-circle
#   The code was adapted and implemented in the same manner as established on the website and I take no credit for creating this. All credits go to charbase.com for providing the code.
#**********************************************************
board_size = 8
counter = 0
Check = -1
PlayerTurn = 1

BLACK = "\u26AB"
WHITE = "\u26AA"

Piece = WHITE
surroundpiece = [ [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1] ]

Player1Counter = 0
Player2Counter = 0

BadMoves = 0                                                                    # To prevent a game from going on indefinitely with players switching sides!
PieceCtn = 4

def Horizontal_lines():
    print("  " * board_size)

def printBoard(board):
    print("    0     1     2     3     4     5     6     7")
    for index in range(8):
        Horizontal_lines()
        print(index, ' ',  board[index], sep='')
    Horizontal_lines()
    return

def PieceCounter(Playboard,Piece,Count):
    
    for i in range(8):
        for j in range(8):
            if Playboard[j][i] == Piece:
                Count += 1
    return Count
            
def flipPiece(board,row,col):
    if board[row][col] == BLACK:
        board[row][col] = WHITE
    else:
        board[row][col] = BLACK
        
def newboard(board):
    newboard = []
    for i in range(8):
        newboard.append(["EM"] * 8)
    newboard[3][3] = BLACK
    newboard[3][4] = WHITE
    newboard[4][3] = WHITE
    newboard[4][4] = BLACK
    return newboard

def makeMove(board,piece,row,col):                              # Makes the players move for them by flipping the pieces then placing his piece at the end.
    board[row][col] = piece

def WithinBoundsCheck(row,col):
    return row >= 0 and row <= 7 and col >= 0 and col <=7

def validMove(Board,piece,row,col):                                             # Definition that handles the majority of the rules in Reversi
    if not WithinBoundsCheck(row,col):
        print("Not a valid move, you are going out of bounds!")                 # Check to make sure the move is valid first.
        return -1
    if Board[row][col] is WHITE or Board[row][col] is BLACK:                    # Check to make sure no piece is already there.
        print("Not a valid move, there is a piece there already!")
        return -1

    if piece == WHITE:                                                          # Figure out whose turn it is and what color is being capture.
        OtherTile = BLACK
    else:
        OtherTile = WHITE

    FlipCheck = -1
                                                            
    for xdir,ydir in surroundpiece:                                             # Creates a x and y direction within the surroundpiece list. This list is used to check all squares surrounding a piece you placed.
        x = col
        y = row
        x += xdir                                                               # Head in the direction defined by the surroundpiece list.
        y += ydir
        if WithinBoundsCheck(x,y) and Board[y][x] == OtherTile:                  # Is the new tile within bounds and occupied by an opposite color piece?
            x += xdir
            y += ydir
            if not WithinBoundsCheck(y,x):                                       # Check if the new x and y spot is within bounds, if it isn't, continue in a new direction.   
                continue
            while Board[y][x] == OtherTile:                                     # If it finds an opposite color pile, continue checking along the path until either it finds an empty tile or your own piece.
                x += xdir
                y += ydir
                if not WithinBoundsCheck(y,x):                                   # Break out of the loop if it walks out of bounds.
                    break
            if not WithinBoundsCheck(y,x):                                       # Check to see if the new x and y spot is still within bounds, if it isn't, continue in a new direction. This checks for edge pieces
                continue
            if Board[y][x] == piece:                                            # If you find your own piece at the end, that means there are enemy pieces in between your new piece and a piece you previously own, capture these pieces.
                while True:
                    x -= xdir
                    y -= ydir
                    if x == col and y == row:
                        break
                    flipPiece(Board,y,x)                            # Flip all these pieces in between your 2 pieces.
                    FlipCheck = 1

    if FlipCheck == -1:                                            # If no flips were done, the move is not valid.
        print ("No Tiles can be flipped, not a valid move!")
        return -1
    makeMove(Playboard,piece,row,col)                        # If all checks pass, allow the player to make that move and capture any pieces found in the list.
    return 1                                                                    # Return a positive number indicating that a successful move was made.

Playboard = newboard(board_size)

print("Welcome to Othello or Reversi! A simple game between 2 players fighting for control over the board!")
print("The objective of the game is to hold more pieces than your opponent or capture all of his pieces.")
print("To place a piece, simply enter the row you want, then the column. The squares will read as such: (Row,Col).")
print("The top left corner is considered (0,0). Bottom Right corner is considered (7,7).")
print("An example: If you want the square (3,2): Enter row as 3, and the column as 2. Row numbers are listed on the lefthand side and column numbers are at the top.")
print("To make a move, the square you pick must allow you to capture an opponent's piece. To capture an opponent's piece,")
print("their pieces must be in between one of your previously placed pieces and your newly placed piece. You can do captures in multiple directions.")
print("Making a move that does not capture an opponent's piece is an illegal move and you are allowed 3 chances to make a legal move.")
print("If you cannot make a move, then after 3 invalid moves, your turn will be skipped.")
print("Once all 64 squares are occupied or a player loses all his pieces, the winner wil be decided!")
print("If both players consecutively make 3 illegal moves (6 illegal moves in total), the game will automatically end and a winner will be decided based on the pieces already placed!")
print("\t\t Good luck!")
print("")

while True:
    
    Player1Counter = PieceCounter(Playboard,WHITE,0)
    Player2Counter = PieceCounter(Playboard,BLACK,0)
    
    printBoard(Playboard)
    
    print("Player 1 (WHITE) pieces:",Player1Counter)
    print("Player 2 (BLACK) pieces:",Player2Counter)

    if Player1Counter == 0 or Player2Counter == 0 or PieceCtn == 64 or BadMoves == 6:                       ##End game if one player lost all his pieces or all pieces have been placed
        break
    
    print("Number of pieces on board:",PieceCtn)
    print("Illegal Moves:",counter)
    
    print("Your turn Player",PlayerTurn)
    
    row = int(input("Enter a row number:"))
    col = int(input("Enter a column number:"))
    
    check = validMove(Playboard,Piece,row,col)                                          # Check the move is valid and send in all the necessary information
    
    if check != -1:
        if PlayerTurn == 1:
            PlayerTurn = 2
            Piece = BLACK
            PieceCtn += 1
            counter = 0
            FlipCheck = -1
            BadMoves = 0
        else:
            PlayerTurn = 1
            Piece = WHITE
            PieceCtn += 1
            counter = 0
            FlipCheck = -1
            BadMoves = 0
    if check == -1:
        counter += 1                    ## If a player fails to make a valid move or cannot make a move after a certain amount of tries, force the other players turn.
        BadMoves += 1
        if counter == 3:
            if PlayerTurn == 1:
                PlayerTurn = 2
                Piece = BLACK
                counter = 0
            else:
                PlayerTurn = 1
                Piece = WHITE
                counter = 0

print("")
if BadMoves == 6:
    print("Both sides made too many illegal moves. It is assumed neither side can make a move!")
if Player1Counter > Player2Counter:
    print("Congratulations Player 1! You hold the most pieces on the board and have won!")
elif Player1Counter < Player2Counter:
    print("Congratulations Player 2! You hold the most pieces on the board and have won!")
else:
    print("Both sides have equal control of the board! It is a tie!")
