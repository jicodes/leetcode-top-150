class Solution:
    def totalNQueens(self, n: int) -> int:
        # Initialize the count of solutions
        self.count = 0

        # Sets to keep track of columns and diagonals that are occupied
        cols = set()
        diag1 = set()  # (\ direction) major diagonals (row - col)
        diag2 = set()  # (/ direction) minor diagonals (row + col)

        def backtrack(row: int):
            # If all rows are processed, we found a solution
            if row == n:
                self.count += 1
                return

            # Try placing a queen in each column of the current row
            for col in range(n):
                # Check if the column and diagonals are not occupied
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # Place the queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                # Move to the next row
                backtrack(row + 1)

                # Remove the queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        # Start the backtracking process from the first row
        backtrack(0)

        return self.count
