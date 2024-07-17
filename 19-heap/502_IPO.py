import heapq
from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        # Create a list of (capital, profit) pairs and sort it by capital
        projects = sorted(zip(capital, profits))
        max_heap = []
        curr_capital = w
        i = 0
        n = len(projects)

        for _ in range(k):
            # Push all projects that can be done with the current capital to the max-heap
            while i < n and projects[i][0] <= curr_capital:
                heapq.heappush(
                    max_heap, -projects[i][1]
                )  # Use a max-heap by pushing negative profits
                i += 1

            # If the heap is empty, break out of the loop
            if not max_heap:
                break

            # Pop the most profitable project from the max-heap
            curr_capital += -heapq.heappop(max_heap)

        return curr_capital
