import random
from IPython.display import clear_output

def display_board(board):
    """Displays the board"""
    clear_output()
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("----------")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("----------")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

def player_input(player):
    """ Gets the player input and ensures its validity"""
    choice = 'Wrong'
    while choice not in ['X', 'O']:
        choice = input(f'Player {player}: Please Choose either "X" or "O": ').upper()
        if choice not in ['X', 'O']:
            print('Invalid Choice please choose X or O: ')
    return choice

def place_marker(board, marker, position):
    """ Places the marker on the board"""
    board[position] = marker
    return board


def win_check(board, mark):
    """Checks if we have a winning match on the board"""

    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # down the middle
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # down the middle
            (board[3] == mark and board[6] == mark and board[9] == mark) or  # down the right side
            (board[3] == mark and board[5] == mark and board[7] == mark) or  # diagonal
            (board[1] == mark and board[5] == mark and board[9] == mark))  # diagonal

def choose_first():
    """ Decides who goes first"""
    first = random.randint(1, 2)
    print( f'Player {first} went first')
    return f'Player {first} went first'

def space_check(board, position):
    """ Checks if the position on the board is free"""
    if board[position] == ' ':
        return True
    return False

def full_board_check(board):
    """ Checks of the board is full"""
    for i in range(1, 10):
       # use the space check function to check each place on the board
        if space_check(board, i):
            return False
    return True

def player_choice(board, whos_turn):
    """ Gets the players choice and makes sure it is a valid choice"""
    choice = 'wrong'
    while choice not in range(1, 9):
        try:
            choice = int(input(f"Player {whos_turn} Choose your next move(Number between 1 and 9): "))
            #Make sure it is a valid choice
            if choice > 9 or choice < 1:
                print('Please choose a number from 1 - 9 Only')
                continue
            # if the space is not free on the board
            if not space_check(board, choice):
                print("Place is already taken. Please choose again")
                choice = 'Wrong'
                continue
        except:
            print("Please enter a digit between 1 and 9 only")
        break
        
    return choice

def replay():
    """ Ask if we want to play again"""
    answer = input("Would you like to play again? Y/N: ")
    if answer == 'Y':
        return True
    return False



if __name__ == '__main__':
    """ Game Logic"""
    print("Welcome to Tic Tac Toe")
    #Initalize board
    game_board = [' ']*10
    PLAYER1 = ''
    PLAYER2 = ''
    #loop to run the game
    while True:
        # See which player is first
        whos_first = choose_first()
        which_player = whos_first[7]
        # if player 1 is first
        if which_player == '1':
            PLAYER1 = True
            # get the player 1 marker
            player1_marker = player_input(which_player)
            # if player1 chose X then player2 is O
            if player1_marker == "X":
                player2_marker = "O"
            else:
                player2_marker = "X"

        # if player 2 is first
        else:
            player2_marker = player_input(which_player)
            PLAYER2 = True
            if player2_marker == 'X':
                player1_marker = 'O'
            else:
                player1_marker = 'X'

        # While no one has won yet
        while not win_check(game_board, player1_marker) and not win_check(game_board, player2_marker):
            display_board(game_board)
            #if the board is full we have a tie
            if full_board_check(game_board):
                print("We have a tie!")
                break
            #player 1's turn
            if PLAYER1:
                turn = 1
                #next move
                player1_move = player_choice(game_board, turn)
                #place marker on the board
                game_board = place_marker(game_board, player1_marker, player1_move)
                # check if player 1 won
                if win_check(game_board, player1_marker):
                    display_board(game_board)
                    print('Player 1 wins!!')
                    break
                PLAYER1 = False
                PLAYER2 = True
                continue
            #player 2's turn
            elif PLAYER2:
                turn = 2
                #next move
                player2_move = player_choice(game_board, turn)
                #place marker on the board
                game_board = place_marker(game_board, player2_marker, player2_move)
                # check if player 2 won
                if win_check(game_board, player2_marker):
                    display_board(game_board)
                    print("Player 2 wins!!")
                    break
                PLAYER2 = False
                PLAYER1 = True
                continue
        #ask if the user wants to play again
        play_again = replay()
        if play_again:
            game_board = [' '] * 10
            continue
        print("Thanks For Playing! See ya next time!")
        break
