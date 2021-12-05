ROWS, COLS = (5, 5)

# Process input file into a list 1D draw list and array of boards
def read_file_input(filename):
    with open(filename) as f:
        board_list = []
        # Read first line containing random number draws into a list
        num_draw_list = [int(num) for num in f.readline().split(',')]

        # Read remaining lines into boards separated by empty newline
        for board in f.read().strip().split("\n\n"):
            final_board = [int(item) for item in board.replace("\n", " ").split()]
            board_list.append(final_board)
    
    return num_draw_list, board_list 

# Generate bingo board using 2D list, containing [value, mark] intialize mark to 0 
def generate_board(board_data):
    # Initialize bingo board
    board = [[[0]*2 for i in range(COLS)] for j in range(ROWS)]
    idx = 0
    # Fill board with numbers
    for i in range(ROWS):
        for j in range(COLS):
            board[i][j][0] = board_data[idx]
            idx += 1
    
    return board

# Print a given board, including its content 
def print_board(board_data):    
    for row in board_data:
        print(row)

# Mark the board at a position containing a matching value with the number drawn
def mark_number_on_board(board, num):
    temp_board = board
    # Search for num and mark position if found
    for i in range(ROWS):
        for j in range(COLS):
            if temp_board[i][j][0] == num:
                temp_board[i][j][1] = 1
                return temp_board

    return temp_board

# Confirm if a winning state has been reached vertically or horizontally
def confirm_win_status(board):
    # Check if rows are fully marked
    for i in range(ROWS):
        mark_sum_row, mark_sum_col = 0, 0
        for j in range(COLS):
            if board[i][j][1] == 1:
                mark_sum_row += 1 
            if board[j][i][1] == 1:
                mark_sum_col += 1 
        if mark_sum_row == COLS or mark_sum_col == ROWS:
            return True
    
    return False

# Compute winning score from umarked numbers on the board
def compute_winning_score(winner_board):
    score_sum = 0
    # Sum all unmarked numbers
    for i in range(ROWS):
        for j in range(COLS):
            if winner_board[i][j][1] == 0:
                score_sum += winner_board[i][j][0]

    return score_sum
        


# Main function
def main():
    completion_time = []
    print('--------Part 1--------')
    draw_list, boards_list = read_file_input('input.txt')

    # Loop through the list of boards
    for bingo_board in boards_list:
        current_board = generate_board(bingo_board)
        # Draw each random number from the list for each board
        for i in range(len(draw_list)):
            current_board = mark_number_on_board(current_board, draw_list[i])
            result = confirm_win_status(current_board)
            if result:
                win_score = compute_winning_score(current_board) * draw_list[i]
                completion_time.append((i, win_score))
                break

    # Print out results       
    # print(completion_time)
    first_board = min(completion_time)
    final_score_first  = first_board[1]
    print(f'First board wins on draw no -> {first_board}')
    print(f'Final score -> {final_score_first}')

    print('--------Part 2--------')
    # print(completion_time)
    last_board = max(completion_time)
    final_score_last  = last_board[1]
    print(f'Last board wins on draw no -> {last_board}')
    print(f'Final score -> {final_score_last}')


if __name__ == '__main__':
    main()