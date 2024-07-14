from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def count_live_neighbors(row, col):
            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            live_neighbors = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (board[r][c] == 1 or board[r][c] == 2):
                    # Count cell as live if it's originally live (1) or was live but is now marked to die (2)
                    live_neighbors += 1
            return live_neighbors

        # First pass to mark the cells with the new states
        for row in range(m):
            for col in range(n):
                live_neighbors = count_live_neighbors(row, col)
                if board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = 2  # Live to dead
                else:
                    if live_neighbors == 3:
                        board[row][col] = 3  # Dead to live

        # Second pass to update the board to the new states
        for row in range(m):
            for col in range(n):
                if board[row][col] == 2:
                    board[row][col] = 0  # Update cell to dead
                elif board[row][col] == 3:
                    board[row][col] = 1  # Update cell to live
