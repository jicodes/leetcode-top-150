class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # If out of bounds or the cell is '0', return
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            # Mark the cell as visited by setting it to '0'
            grid[r][c] = "0"
            # Visit all adjacent cells (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is '1', it's part of an island
                if grid[r][c] == "1":
                    num_islands += 1
                    # Perform DFS to mark the entire island
                    dfs(r, c)

        return num_islands


# Example usage
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]

sol = Solution()
print(sol.numIslands(grid))  # Output: 3
