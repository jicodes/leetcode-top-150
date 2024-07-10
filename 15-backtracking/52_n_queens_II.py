class Solution:
    def totalNQueens(self, n: int) -> int:
        # Initialize the count of solutions
        self.count = 0

        # Helper function to check if placing a queen at (row, col) is valid
        def is_valid(board, row, col):
            # Check column
            for i in range(row):
                if board[i] == col:
                    return False
            # Check diagonal /
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i] == j:
                    return False
            # Check diagonal \
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
                if board[i] == j:
                    return False
            return True

        # Backtracking function to place queens
        def backtrack(row, board):
            # If all queens are placed, increment the count
            if row == n:
                self.count += 1
                return
            # Try placing a queen in each column of the current row
            for col in range(n):
                if is_valid(board, row, col):
                    # Place the queen
                    board[row] = col
                    # Move to the next row
                    backtrack(row + 1, board)
                    # Backtrack by resetting the current position
                    board[row] = -1

        # Initialize the board with -1 (indicating no queens placed)
        board = [-1] * n
        # Start backtracking from the first row
        backtrack(0, board)

        return self.count
