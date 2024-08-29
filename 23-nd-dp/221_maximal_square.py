from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        # DP table where dp[i][j] represents the side length of the largest square ending at (i, j).
        dp = [[0] * n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # Initialize first row/column
                    else:
                        # Update dp[i][j] as the minimum of the three neighbors plus one
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_side = max(max_side, dp[i][j])  # Track the maximum side length

        return max_side * max_side  # Return the area of the largest square
