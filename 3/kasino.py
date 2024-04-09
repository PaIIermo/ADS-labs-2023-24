def read_tokens(path):
    try:
        with open(path, 'r') as file:
            content = file.read().strip()
            number_list = [int(char) for char in content]
        return number_list
    except FileNotFoundError:
        print(f"Súbor nebol nájdený: {path}")

def max_win(tokens):
    n = len(tokens)
    dp = [[0] * n for _ in range (n)]
    for length in range(2, n+2, 2):
        for i in range(n-length+1):
            j = i+length-1
            if i == j:
                dp[i][j] = tokens[i]
            else:
                left_choice = tokens[i] + ((dp[i+2][j] if i+2 <= j else 0) if tokens[i+1] > tokens[j] else (dp[i+1][j-1] if i+1 <= j-1 else 0))
                right_choice = tokens[j] + ((dp[i+1][j-1] if i+1 <= j-1 else 0) if tokens[i] > tokens[j-1] else (dp[i][j-2] if i <= j-2 else 0))

                dp[i][j] = max(left_choice, right_choice)
    print(dp)
    return dp[0][n-1]

file = 'zetony.txt'

tokens = read_tokens(file)
#tokens = [1, 2, 1, 1, 2, 9, 6, 3]
win = max_win(tokens)
total = sum(tokens)

print(f"Total: {total}")
print(f"Win: {win}")
print(f"Dealer takes: {total - win}")