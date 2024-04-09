# 1 
# -------------------------------------------------------------------

def load_matrix_from_file(path):
    with open(path, 'r') as file:
        rows = int(file.readline().strip())
        cols = int(file.readline().strip())
        matrix = [list(map(int, file.readline().strip().split(' '))) for _ in range(rows)]

    return matrix

def select_elements_closest_to_zero(matrix, group_size=10):
    total_sum = 0
    selected_elements = []
    num_rows = len(matrix)

    def find_best_combination_for_group(group):
        from itertools import product

        combinations = list(product(*group))
        best_combination = min(combinations, key=lambda x: abs(sum(x)))
        #print(sum(best_combination))
        return best_combination

    for i in range(0, num_rows, group_size):
        group = matrix[i:i+group_size]
        print(group)
        best_combination = find_best_combination_for_group(group)
        selected_elements.extend(best_combination)
        total_sum += sum(best_combination)

    return selected_elements, total_sum

filepath = "task1_data.txt"
choices, total_sum = select_elements_closest_to_zero(load_matrix_from_file(filepath))

print(total_sum - choices[-1])
print(choices[-1])
print(total_sum)
