from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create adjacency list for the graph
        graph = defaultdict(list)
        for dest, src in prerequisites:
            graph[src].append(dest)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses

        def dfs(course):
            if visit[course] == 1:  # cycle detected, visiting again in the same path
                return False
            if visit[course] == 2:  # already visited
                return True

            # Mark as visiting
            visit[course] = 1

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            # Mark as visited(fully processed)
            visit[course] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
