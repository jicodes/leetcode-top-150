from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # List to store the result combinations
        result = []

        # Backtracking function to generate combinations
        def backtrack(start, path):
            # If the path length is equal to k, we have a complete combination
            if len(path) == k:
                result.append(path[:])
                return

            # Loop through the numbers from start to n
            for i in range(start, n + 1):
                path.append(i)  # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()  # Un-choose

        # Initiate backtracking with an empty path and starting index of 1
        backtrack(1, [])

        return result


# Example usage
solution = Solution()
n = 4
k = 2
print(
    solution.combine(n, k)
)  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
