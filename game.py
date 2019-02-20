player1 = ""
player2 = ""
game_over = False
#Intro Game
def Start(player1,player2):
    print("Welcome to the world's BEST game of Tic Tac Toe!!")

    #Set player 1 to an X or an O (make sure they don't put something else)
    while player1 != "X" and player1 != "O":
        player1 = input("Player 1, do you want X or O? ").upper()
        if player1 != "X" and player1 != "O":
            print("You need to put an X or an O")
            continue

    #set player 2 variable
    if player1 == "X":
        print("That means Player 2 is O\n")
        player2 = "O"
    elif player1 == "O":
        print("That means Player 2 is X\n")
        player2 = "X"

    #returns player variables to change global scope
    return player1,player2

#Starts game
player1,player2 = Start(player1,player2)

def DisplayBoard(board):
    print(f" {board[0]} | {board[1]} | {board[2]} \n---|---|---\n {board[3]} | {board[4]} | {board[5]} \n---|---|---\n {board[6]} | {board[7]} | {board[8]} \n")

board = [" "," "," "," "," "," "," ",' ',' ',' ']
DisplayBoard(board)
player1_turn = True
winner = ""

def GameOverFalse():
    if board.count("X") >= 3 or board.count("O") >= 3: 
        if board[0] == board[1] == board[2] or board[0] == board[4] == board[8] or board[0] == board[3] == board[6] or board[6] == board[7] == board[8] or board[2] == board[5] == board[8]:
            xcount = board.count("X")
            ocount = board.count("O")

            global winner
            if xcount > ocount:
                if player1 == "X":
                    #print("Player 1 WINS!!!!")
                    winner = "Player 1 "
                    return True
                elif player1 == "O":
                    winner = "Player 2 "
                    return True
            elif ocount > xcount:
                if player1 == "O":
                    winner = "Player 1 "
                    return True
                elif player1 == "X":
                    winner = "Player 2 "
                    return True
        else:
            return False
    else:
        return False

#Main Game Loop
while True:
    if GameOverFalse() ==  False:
        if player1_turn:
            #GameOverFalse()
            position1 = int(input("Player 1, choose a position (1-9) "))
            if board[position1-1] != player1 and board[position1-1] != player2:
                board[position1-1] = player1
                player1_turn = False
                DisplayBoard(board)
                GameOverFalse()
                continue
        else:
            #GameOverFalse()
            position2 = int(input("Player 2, choose a position (1-9) "))
            if board[position2-1] != player1 and board[position2-1] != player2:
                board[position2-1] = player2
                player1_turn = True
                DisplayBoard(board)
                GameOverFalse()
                continue

        #GameOverFalse()
    else:
        print(f" {winner} WINS!!!")
        break
    
