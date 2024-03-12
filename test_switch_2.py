import random

# Function to read the initial state from a file
def read_initial_state(file_path: str) -> [int]:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Adjust for 1-indexing
        initial_state = [int(line.strip()) - 1 for line in lines if not line.startswith('#')]
    return initial_state

# Function to find the number of conflicts for a queen
def count_conflicts(board, row, col):
    conflicts = 0
    for i in range(len(board)):
        if i != row:
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                conflicts += 1
    return conflicts

# Function to find the best column for a queen in the given row
def choose_best_column(board, row):
    min_conflicts = len(board)
    best_columns = []
    for col in range(len(board)):
        conflicts = count_conflicts(board, row, col)
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            best_columns = [col]
        elif conflicts == min_conflicts:
            best_columns.append(col)
    return random.choice(best_columns), min_conflicts

# Main function to solve the N-Queens problem
def solve_n_queens(file_path: str):
    board = read_initial_state(file_path)
    max_iterations = 50000
    for _ in range(max_iterations):
        # Find the row with the highest number of conflicts
        row_conflicts = [(row, count_conflicts(board, row, board[row])) for row in range(len(board))]
        row_conflicts = sorted(row_conflicts, key=lambda x: x[1], reverse=True)
        
        # If there's no conflict, the solution is found
        if row_conflicts[0][1] == 0:
            # Adjust for 1-indexing in the final result
            return [col + 1 for col in board]
        
        # Choose a random queen with the highest conflicts to move
        row = random.choice([row for row, conflicts in row_conflicts if conflicts == row_conflicts[0][1]])
        # Find the best column for this queen
        new_col, _ = choose_best_column(board, row)
        board[row] = new_col

    # Adjust for 1-indexing in the final result if solution is not complete
    return [col + 1 for col in board]  # Return the final board (might not be a solution if max_iterations reached)

# Example usage
file_path = 'boardSize1000.txt'  # Replace with your actual file path
n_queens_solution = solve_n_queens(file_path)
print("Final board configuration:", n_queens_solution)
