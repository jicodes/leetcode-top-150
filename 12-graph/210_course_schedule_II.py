from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Create a graph and a list to keep track of in-degrees
        graph = defaultdict(list)
        in_degrees = [0] * numCourses

        # Populate the graph and in-degrees list
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degrees[dest] += 1

        # Initialize the queue with courses having zero in-degrees
        queue = deque([i for i in range(numCourses) if in_degrees[i] == 0])

        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for neighbor in graph[course]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # If the order contains all the courses, return it. Otherwise, return an empty array.
        return order if len(order) == numCourses else []
