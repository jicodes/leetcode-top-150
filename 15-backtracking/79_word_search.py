from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def backtrack(row, col, index):
            # If we have found the word, return True
            if index == len(word):
                return True

            # If out of bounds or character doesn't match, prune the search
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] != word[index]
            ):
                return False

            # Mark the cell as visited by replacing the character with a placeholder
            temp, board[row][col] = board[row][col], "#"

            # Explore all possible directions
            found = (
                backtrack(row + 1, col, index + 1)
                or backtrack(row - 1, col, index + 1)
                or backtrack(row, col + 1, index + 1)
                or backtrack(row, col - 1, index + 1)
            )

            # Restore the original value
            board[row][col] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
