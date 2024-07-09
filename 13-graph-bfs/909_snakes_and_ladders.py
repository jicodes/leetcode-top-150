from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_board_value(num):
            row, col = divmod(num - 1, n)
            if row % 2 == 0:
                return board[n - 1 - row][col]
            else:
                return board[n - 1 - row][n - 1 - col]

        visited = set()
        queue = deque([(1, 0)])  # (current position, number of moves)

        while queue:
            current, moves = queue.popleft()

            for i in range(1, 7):  # simulate a dice roll
                next_pos = current + i
                if next_pos > n * n:
                    continue

                board_value = get_board_value(next_pos)
                if board_value != -1:
                    next_pos = board_value

                if next_pos == n * n:
                    return moves + 1

                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))

        return -1


# This problem is confusing, doesn't help, just skip it.
