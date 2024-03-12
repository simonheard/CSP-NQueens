def solve_n_queens(n):
    def is_safe(queen_position, other_queens):
        for row, col in enumerate(other_queens):
            if col == queen_position or abs(col - queen_position) == len(other_queens) - row:
                return False
        return True

    def place_queens(n, row=0, positions=[]):
        if row == n:
            return [positions]
        solutions = []
        for col in range(n):
            if is_safe(col, positions):
                for solution in place_queens(n, row + 1, positions + [col]):
                    solutions.append(solution)
        return solutions

    # Start the search with no queens placed.
    solutions = place_queens(n)
    if solutions:
        print("Solutions found:", len(solutions))
        for solution in solutions[:1]:  # Print the first solution, if available
            print(solution)
    else:
        print("No solution exists")

# Test with a small n for demonstration, e.g., n=4
solve_n_queens(100)