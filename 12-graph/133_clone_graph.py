from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        visited = {}  # Dictionary to store cloned nodes

        def clone(node):
            if node in visited:
                return visited[node]

            # Create a new node with the same value
            cloned_node = Node(node.val)

            # Mark the original node as visited
            visited[node] = cloned_node

            # Recursively clone the neighbors
            cloned_node.neighbors = [clone(neighbor) for neighbor in node.neighbors]

            return cloned_node

        return clone(node)
