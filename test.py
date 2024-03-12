import itertools
import random
from typing import List

# AC3 algorithm for constraint propagation
def AC3(csp):
    queue = [(xi, xk) for xi in csp.variables for xk in csp.neighbors[xi]]
    while queue:
        (xi, xk) = queue.pop(0)
        if revise(csp, xi, xk):
            if not csp.domains[xi]:
                return False
            for xj in csp.neighbors[xi]:
                if xj != xk:
                    queue.append((xj, xi))
    return True

def revise(csp, xi, xk):
    revised = False
    for x in csp.domains[xi][:]:
        if not any([csp.constraints(xi, x, xk, y) for y in csp.domains[xk]]):
            csp.domains[xi].remove(x)
            revised = True
    return revised

# CSP representation of N-Queens
class NQueensCSP:
    def __init__(self, n, initial_assignment=None):
        self.variables = list(range(n))
        self.domains = {var: list(range(n)) for var in self.variables}
        self.neighbors = {var: [other_var for other_var in self.variables if other_var != var] for var in self.variables}
        self.constraints = lambda var1, val1, var2, val2: val1 != val2 and abs(var1 - var2) != abs(val1 - val2)
        if initial_assignment:
            for var, val in enumerate(initial_assignment):
                self.domains[var] = [val - 1]  # Adjust for 1-indexing
                
    def __str__(self):
        return f"variables: ({self.variables}), domains=({self.domains}), neighbors=({self.neighbors})"
                
# Heuristic functions
def select_unassigned_variable(csp, assignment):
    unassigned_vars = [var for var in csp.variables if var not in assignment]
    # MRV heuristic
    return min(unassigned_vars, key=lambda var: len(csp.domains[var]), default=None)

def order_domain_values(var, assignment, csp):
    # LCV heuristic
    return sorted(csp.domains[var], key=lambda val: sum(1 for neighbor in csp.neighbors[var] if val in csp.domains[neighbor]))

# Backtracking search algorithm
def backtrack(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(csp, assignment)
    if var is None:
        return None
    for value in order_domain_values(var, assignment, csp):
        if all(csp.constraints(var, value, other_var, assignment[other_var]) for other_var in assignment if other_var in csp.neighbors[var]):
            assignment[var] = value
            result = backtrack(assignment.copy(), csp)
            if result is not None:
                return result
            del assignment[var]
    return None

def backtracking_search(csp):
    return backtrack({}, csp)

# Main function to read input and solve N-Queens
def solve_n_queens(filename):
    with open(filename, 'r') as file:
        initial_assignment = [int(line.strip()) for line in file if line[0].isdigit()]
    n = len(initial_assignment)
    
    csp = NQueensCSP(n, initial_assignment)
    print(csp)
    AC3(csp)
    print(csp)
    # solution = backtracking_search(csp)
    # if solution is not None:
    #     # Convert solution to 1-indexing for consistency with input
    #     solution = [pos + 1 for pos in solution.values()]
    #     print("Solution:", solution)
    # else:
    #     print("No solution exists")

# Replace 'input.txt' with your file path
solve_n_queens('board1.txt')