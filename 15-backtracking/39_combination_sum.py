from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Initialize an empty list to store the result
        result = []

        # Define a recursive backtracking function
        def backtrack(start, path, target):
            # If the target becomes negative, stop exploring this path
            if target < 0:
                return
            # If the target becomes zero, add the current combination to the result
            if target == 0:
                result.append(path)
                return
            # Iterate through the candidates starting from the 'start' index
            for i in range(start, len(candidates)):
                # Explore the next candidate by adding it to the path
                backtrack(i, path + [candidates[i]], target - candidates[i])

        # Start the backtracking process from the beginning of the candidates list
        backtrack(0, [], target)

        return result
