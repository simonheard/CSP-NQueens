import random

# AC3 algorithm for constraint propagation
def AC3(queens):
    queue = [(row, col) for row in range(len(queens)) for col in range(len(queens)) if col != queens[row]]
    while queue:
        (row, col) = queue.pop()
        if revise(queens, row, col):
            if len(queens) == 0:
                return False
            for i in range(len(queens)):
                if i != row:
                    queue.append((i, queens[row]))
    return True

# Revise function for AC3
def revise(queens, row, col):
    revised = False
    if conflicts(row, col, queens) < conflicts(row, queens[row], queens):
        queens[row] = col
        revised = True
    return revised

# Check the number of conflicts for the queen at (row, col)
def conflicts(row, col, queens):
    count = 0
    for i in range(len(queens)):
        if i != row:
            if queens[i] == col or abs(i - row) == abs(queens[i] - col):
                count += 1
    return count

# Heuristic: Choose the most constrained row (the row with the queen having the most conflicts)
def select_most_constrained_row(queens):
    max_conflicts = 0
    most_constrained_rows = []
    for row in range(len(queens)):
        num_conflicts = conflicts(row, queens[row], queens)
        if num_conflicts > max_conflicts:
            max_conflicts = num_conflicts
            most_constrained_rows = [row]
        elif num_conflicts == max_conflicts:
            most_constrained_rows.append(row)
    return random.choice(most_constrained_rows) if most_constrained_rows else None

# Main CSP solving algorithm
def solve_n_queens(queens):
    for _ in range(len(queens)**2):
        if all(conflicts(row, queens[row], queens) == 0 for row in range(len(queens))):
            return queens  # Solved
        row = select_most_constrained_row(queens)
        if row is not None:
            min_conflicts = float('inf')
            best_columns = []
            for col in range(len(queens)):
                num_conflicts = conflicts(row, col, queens)
                if num_conflicts < min_conflicts:
                    min_conflicts = num_conflicts
                    best_columns = [col]
                elif num_conflicts == min_conflicts:
                    best_columns.append(col)
            chosen_col = random.choice(best_columns)
            queens[row] = chosen_col
    return None  # No solution found

# Reading the initial state from a file
def read_initial_state(filename):
    with open(filename, 'r') as file:
        queens = []
        for line in file:
            if not line.startswith('#'):  # Ignore comments
                queens.append(int(line.strip()) - 1)  # Convert to 0 indexing
    return queens

# Example usage
filename = 'board1.txt'
initial_queens = read_initial_state(filename)
solution = solve_n_queens(initial_queens)
if solution:
    print("Solution found:")
    for row in solution:
        print(row + 1)  # Convert back to 1 indexing for output
else:
    print("No solution found.")