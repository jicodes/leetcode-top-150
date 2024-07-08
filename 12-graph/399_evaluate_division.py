from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)

        # Build the graph
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set()

            while queue:
                current, current_product = queue.popleft()
                if current == end:
                    return current_product
                visited.add(current)
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        queue.append((neighbor, current_product * value))

            return -1.0

        results = []
        for dividend, divisor in queries:
            if dividend == divisor and dividend in graph:
                results.append(1.0)
            else:
                results.append(bfs(dividend, divisor))

        return results
