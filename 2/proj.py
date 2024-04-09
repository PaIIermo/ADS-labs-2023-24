def calculate_min_penalty(file_path):
    with open(file_path, 'r') as file:
        distances = [int(line.strip()) for line in file]
    distances.insert(0, 0)  

    n = len(distances)
    dp = [float('inf')] * n
    dp[0] = 0  

    for i in range(1, n):
        for j in range(i):
            penalty = (400 - (distances[i] - distances[j])) ** 2
            dp[i] = min(dp[i], dp[j] + penalty)
    return dp

file_path = "data.txt"
min_penalty = calculate_min_penalty(file_path)
print(f"Minimum total penalty: {min_penalty}")
