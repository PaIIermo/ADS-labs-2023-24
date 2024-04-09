import numpy as np

def load_items_from_file(file_path):
    items = []
    with open(file_path, 'r') as file:
        for line in file:
            value, weight, volume = map(int, line.strip().split(','))
            items.append((value, weight, volume))
    return items

def find_chosen_items_with_index(items, dp, max_weight, max_volume):
    chosen_items_with_index = []
    i, w, v = len(items), max_weight, max_volume
    while i > 0:
        item_value, item_weight, item_volume = items[i-1]
        if dp[i][w][v] != dp[i-1][w][v]: 
            chosen_items_with_index.append((i, items[i-1]))
            w -= item_weight
            v -= item_volume
        i -= 1
    return chosen_items_with_index[::-1]  



def knapsack_max(items, max_weight, max_volume):
    
    n = len(items)
    dp = np.zeros((n + 1, max_weight + 1, max_volume + 1), dtype=int)

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            for v in range(1, max_volume + 1):

                # Option 1 - not taking
                dp[i][w][v] = dp[i-1][w][v]

                item_value, item_weight, item_volume = items[i-1]

                # Option 2 - if constraints allow, check if the best path 
                # for the current constraints includes the item
                if item_weight <= w and item_volume <= v:
                    dp[i][w][v] = max(dp[i][w][v], dp[i-1][w-item_weight][v-item_volume] + item_value)

    chosen_items_with_index = find_chosen_items_with_index(items, dp, max_weight_limit, max_volume_limit)

    # Print chosen items with their line numbers
    for index, item in chosen_items_with_index:
        print(f"Line {index}: Item {item}")
    return dp[n][max_weight][max_volume]            


file_path = 'jewels.txt'
items = load_items_from_file(file_path)

max_weight_limit = 200
max_volume_limit = 80
max_value_with_volume = knapsack_max(items, max_weight_limit, max_volume_limit)

print(max_value_with_volume)

