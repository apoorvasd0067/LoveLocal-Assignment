def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side ** 2

# Take user input for the binary matrix
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = []
for i in range(m):
    row = input(f"Enter row {i+1} (0's and 1's separated by space): ").split()
    matrix.append(row)

# Example usage:
result = maximalSquare(matrix)
print(result)
