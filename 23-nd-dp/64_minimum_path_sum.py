from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns
        m, n = len(grid), len(grid[0])

        # Iterate through the grid, updating each cell
        for i in range(m):
            for j in range(n):
                # If we're not on the top row, add the value from the cell above
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i > 0:  # Only add from above if not in the first column
                    grid[i][j] += grid[i - 1][j]
                elif j > 0:  # Only add from the left if not in the first row
                    grid[i][j] += grid[i][j - 1]

        # The bottom-right corner now contains the minimum path sum
        return grid[m - 1][n - 1]
