# Peg Solitaire Game.
# Created in December 2021.
# Author Christos-Grigorios Gkovaris

# Introductory message.
print('Welcome to the Peg Solitaire Game!')

# Initial board setup.
game_state = [
    [' ', '', '1', '2', '3', '4', '5', '6', '7'],
    ['A', '', ' ', ' ', '1', '1', '1', ' ', ' '],
    ['B', '', ' ', ' ', '1', '1', '1', ' ', ' '],
    ['C', '', '1', '1', '1', '1', '1', '1', '1'],
    ['D', '', '1', '1', '1', '0', '1', '1', '1'],
    ['E', '', '1', '1', '1', '1', '1', '1', '1'],
    ['F', '', ' ', ' ', '1', '1', '1', ' ', ' '],
    ['G', '', ' ', ' ', '1', '1', '1', ' ', ' ']]

# Display the board.
def display_board(state):
    for line in state:
        print(' '.join(line))

# Handle player moves.
def handle_move(state):
    if not any_valid_moves(state):
        print('No valid moves left, game over!')
        return
    
    user_input = input('Enter peg position and direction (L, R, U, D): ').upper()
    command = list(user_input)

    if not is_valid_command(command):
        handle_move(state)
    else:
        if execute_move(state, command):
            display_board(state)
        handle_move(state)

# Get alphabetical index.
def alphabet_index(char):
    if 'A' <= char <= 'Z':
        return ord(char) - ord('A') + 1
    return -1 

# Validate the command.
def is_valid_command(command):
    if (command[0] not in 'ABCDEFG') or (command[1] not in '1234567') or (command[2] not in 'LRUD'):
        print('Invalid input, try again.')
        return False

    row_idx = alphabet_index(command[0])
    col_idx = int(command[1])

    if (command[0] in 'ABFG') and ((col_idx == 3 and command[2] == 'L') or (col_idx == 5 and command[2] == 'R') or (col_idx in [1, 2, 6, 7])):
        print('Move not possible, no peg present.')
        return False

    if (col_idx in [1, 2, 6, 7]) and ((command[2] == 'U' and row_idx < 3) or (command[2] == 'D' and row_idx > 5)):
        print('Invalid move for given position.')
        return False

    return True

# Execute the move.
def execute_move(state, command):
    row_idx = alphabet_index(command[0])
    col_idx = int(command[1])+1

    if command[2] == 'L':
        if col_idx > 2 and state[row_idx][col_idx] == '1' and state[row_idx][col_idx - 1] == '1' and state[row_idx][col_idx - 2] == '0':
            state[row_idx][col_idx] = '0'
            state[row_idx][col_idx - 1] = '0'
            state[row_idx][col_idx - 2] = '1'
            return True
    elif command[2] == 'R':
        if col_idx < 6 and state[row_idx][col_idx] == '1' and state[row_idx][col_idx + 1] == '1' and state[row_idx][col_idx + 2] == '0':
            state[row_idx][col_idx] = '0'
            state[row_idx][col_idx + 1] = '0'
            state[row_idx][col_idx + 2] = '1'
            return True
    elif command[2] == 'U':
        if row_idx > 2 and state[row_idx][col_idx] == '1' and state[row_idx - 1][col_idx] == '1' and state[row_idx - 2][col_idx] == '0':
            state[row_idx][col_idx] = '0'
            state[row_idx - 1][col_idx] = '0'
            state[row_idx - 2][col_idx] = '1'
            return True
    elif command[2] == 'D':
        if row_idx < 6 and state[row_idx][col_idx] == '1' and state[row_idx + 1][col_idx] == '1' and state[row_idx + 2][col_idx] == '0':
            state[row_idx][col_idx] = '0'
            state[row_idx + 1][col_idx] = '0'
            state[row_idx + 2][col_idx] = '1'
            return True

    print('Move is not valid!')
    return False

# Check for any valid moves.
def any_valid_moves(state):
    for row in range(1, 8):
        for col in range(2, 8):
            if state[row][col] == '1':
                if col > 2 and state[row][col - 1] == '1' and state[row][col - 2] == '0':
                    return True
                if col < 6 and state[row][col + 1] == '1' and state[row][col + 2] == '0':
                    return True
                if row > 2 and state[row - 1][col] == '1' and state[row - 2][col] == '0':
                    return True
                if row < 6 and state[row + 1][col] == '1' and state[row + 2][col] == '0':
                    return True
    return False

# Count remaining pegs.
def count_pegs():
    total_pegs = 0
    for row in range(0, 8):
        total_pegs += game_state[row].count('1')
    return total_pegs

# End the game if no moves left.
def conclude_game():
    if not any_valid_moves(game_state):
        print(f'Game over! Remaining pegs: {count_pegs()}')

# Main game function.
def play_game():
    display_board(game_state)
    handle_move(game_state)
    conclude_game()

play_game()
