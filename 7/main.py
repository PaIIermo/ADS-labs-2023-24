import random
import sys
import time

def evaluate_clause(clause, values):
    return any(values[abs(x)-1] ^ (x < 0) for x in clause)

def evaluate_formula(formula, values):
    return all(evaluate_clause(clause, values) for clause in formula)

def simple_3_sat_solver(formula, n):
    start_time = time.time()
    for iteration in range(3 * n): 
        values = [random.randint(0, 1) for _ in range(n)]
        if evaluate_formula(formula, values):
            return True, values, iteration + 1, time.time() - start_time
    return False, None, iteration + 1, time.time() - start_time

def pick_unsatisfied_clause(formula, values):
    unsatisfied_clauses = [clause for clause in formula if not evaluate_clause(clause, values)]
    return random.choice(unsatisfied_clauses) if unsatisfied_clauses else None

def schoening_algorithm(formula, n):
    start_time = time.time()
    total_flips = 0
    successful_flips = 0
    for iteration in range(3 * n):
        values = [random.randint(0, 1) for _ in range(n)]
        local_flips = 0  # Flips for this iteration
        for _ in range(3 * n):
            if evaluate_formula(formula, values):
                return True, values, iteration + 1, time.time() - start_time, total_flips, local_flips
            clause = pick_unsatisfied_clause(formula, values)
            if clause is not None:
                literal_to_flip = random.choice(clause)
                values[abs(literal_to_flip) - 1] = 1 - values[abs(literal_to_flip) - 1]
                total_flips += 1
                local_flips += 1
    return False, None, iteration + 1, time.time() - start_time, total_flips, successful_flips

def read_formula_from_file(filename):
    with open(filename, 'r') as file:
        formula = []
        for line in file:
            clause = list(map(int, line.strip().split()))
            formula.append(clause)
        return formula
    
def generate_random_3sat_formula(n, m):
    formula = []
    for _ in range(m):
        clause = set()
        while len(clause) < 3:
            literal = random.randint(1, n) * random.choice([-1, 1])
            if -literal not in clause:
                clause.add(literal)
        formula.append(list(clause))
    return formula

def main():
    '''
    if len(sys.argv) != 3:
        print("Usage: python 3sat_solver.py <algorithm_number> <file_path>")
        sys.exit(1)

    algorithm_number = sys.argv[1]
    file_path = sys.argv[2]
    formula = read_formula_from_file(file_path)
    n = max(abs(literal) for clause in formula for literal in clause)
    '''
    if len(sys.argv) != 4:
        print("Usage: python 3sat_solver.py <algorithm_number> <num_literals> <num_clauses>")
        sys.exit(1)

    algorithm_number = sys.argv[1]
    num_literals = int(sys.argv[2])
    num_clauses = int(sys.argv[3])

    # Generate the formula with n literals and m clauses
    formula = generate_random_3sat_formula(num_literals, num_clauses)
    print(formula)

    if algorithm_number in ['1', '3']:
        print("Running the simple algorithm:")
        is_solvable_simple, assignment_simple, iterations_simple, time_simple = simple_3_sat_solver(formula, num_literals)
        print(f"Solvable: {is_solvable_simple}")
        if is_solvable_simple:
            print(f"Assignment: {assignment_simple}")
        print(f"Iterations: {iterations_simple}")
        print(f"Time taken: {time_simple:.6f} seconds")

    if algorithm_number in ['2', '3']:
        if algorithm_number == '2':
            print("Running Schöning's algorithm:")
        else:
            print("\nRunning Schöning's algorithm:")
        is_solvable_schoening, assignment_schoening, iterations_schoening, time_schoening, total_flips, successful_flips = schoening_algorithm(formula, num_literals)
        print(f"Solvable: {is_solvable_schoening}")
        print(f"Total flips: {total_flips}")
        if is_solvable_schoening:
            print(f"Flips in successful iteration: {successful_flips}")
            print(f"Assignment: {assignment_schoening}")
        print(f"Iterations: {iterations_schoening}")
        print(f"Time taken: {time_schoening:.6f} seconds")

    if algorithm_number == '3':
        print("\nComparison:")
        print("Simple Algorithm - Time: {:.6f} seconds, Iterations: {}".format(time_simple, iterations_simple))
        print("Schöning's Algorithm - Time: {:.6f} seconds, Total flips: {}".format(time_schoening, total_flips))

if __name__ == "__main__":
    main()
