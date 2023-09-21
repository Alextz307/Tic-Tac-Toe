def retrieve_name(message):
    name = input(message)
    
    print()
    
    return name


def validate_input(valid_answers, message):
    result = 'invalid'
    
    while result not in valid_answers:
        result = input(message)

        if result not in valid_answers:
            print('Sorry, your choice is invalid, please enter something else!')
            print()
            
    print()
            
    return result


def choose_symbols(names):
    first_player = validate_input(['X', 'O', 'x', 'o'], f'{names[0]}: Do you want to be X or O? ').upper()
    
    second_player = 'O'
    
    if first_player == 'O':
        second_player = 'X'
    
    return first_player, second_player


def round_setup():
    names = ['Player 1', 'Player 2']
    
    for i in range(2):
        names[i] = retrieve_name(f'Player {i + 1}, please enter your name: ')

    
    first_player, second_player = choose_symbols(names)

    current_player = (second_player == 'X')

    print(f'{names[current_player]} will go first!')
    print()
    
    game_start = validate_input(['y', 'Y', 'n', 'N'], 'Are you ready to play? Enter Y or N. ')
            
    return game_start.lower() == 'y', names, current_player


def board_setup():
    patterns = ['   |   |   ', '-----------']
    board = []
    
    for i in range(3):
        for j in range(3):
            board.append(list(patterns[0]))
            
        if i != 2:
            board.append(list(patterns[1]))
            
            
    return board


def print_board(board):
    for row in board:
        print(*row)
    
    print()


def validate_position(name, used):
    result = 'invalid'
    
    while (not result.isdigit()) or (int(result) not in range(1, 10)) or used[int(result) - 1]:
        result = input(f'{name}, please enter an unused position from 1 to 9. ')
        print()
            
        if (not result.isdigit()) or (int(result) not in range(1, 10)):
            print('Your choice is not from 1 to 9, please enter another one.')
            print()
        elif used[int(result) - 1]:
            print('The position is already used, please enter another one.')
            print()
            
    print()
            
    return int(result)


def check_row(board, row):
    return board[row][1] == board[row][5] and board[row][5] == board[row][9]


def check_column(board, column):
    return board[1][column] == board[5][column] and board[5][column] == board[9][column]


def check_diagonals(board):
    principal = (board[1][1] == board[5][5] and board[5][5] == board[9][9] and board[1][1] != ' ')
    
    secondary = (board[1][9] == board[5][5] and board[5][5] == board[9][1] and board[1][9] != ' ')
    
    return principal or secondary


def play_round():
    ready, names, current_player = round_setup()
    
    if not ready:
        return False
    
    board = board_setup()
    
    used = [False] * 9
    empty_cells = 9
    
    symbol = 'X'
    is_win = False
    
    index = {
        1: (1, 1),
        2: (1, 5),
        3: (1, 9),
        4: (5, 1),
        5: (5, 5),
        6: (5, 9),
        7: (9, 1),
        8: (9, 5),
        9: (9, 9)
    }
    
    while empty_cells > 0 and not is_win:
        print_board(board)
        
        position = validate_position(names[current_player], used)
        
        x, y = index[position][0], index[position][1]
        
        board[x][y] = symbol
        
        if check_row(board, x) or check_column(board, y) or check_diagonals(board):
            print_board(board)
            
            print(f'Congratulations, {names[current_player]}, you won!')
            is_win = True
            
            
        used[position - 1] = True
        empty_cells -= 1
        current_player ^= 1
        
        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'
        
        
    if not is_win:
        print_board(board)
        
        print('This round resulted in a tie!')
        
    print()
        
    result = validate_input(['y', 'Y', 'n', 'N'], 'Do you want to keep playing? ')
    
    return result.lower() == 'y'


def play_game():    
    print('Welcome to Tic Tac Toe!')
    print()
    
    print('The board indexing follows this scheme: ')
    
    board = board_setup()
    
    board[1][1] = '1'
    board[1][5] = '2'
    board[1][9] = '3'
    board[5][1] = '4'
    board[5][5] = '5'
    board[5][9] = '6'
    board[9][1] = '7'
    board[9][5] = '8'
    board[9][9] = '9'
    
    print_board(board)
    
    play = True
    
    while play:
        play = play_round()


def main():
    play_game()


if __name__ == '__main__':
    main()
