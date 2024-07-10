from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the result list to store valid combinations
        result = []

        # Define a backtracking function to generate combinations
        def backtrack(curr_string, open_count, close_count):
            # Base case: If the current string is of length 2 * n, add it to the result
            if len(curr_string) == 2 * n:
                result.append(curr_string)
                return
            # If we can add an open parenthesis, do so and recurse
            if open_count < n:
                backtrack(curr_string + "(", open_count + 1, close_count)
            # If we can add a close parenthesis, do so and recurse
            if close_count < open_count:
                backtrack(curr_string + ")", open_count, close_count + 1)

        # Start the backtracking process with an empty string and zero counts for open and close parentheses
        backtrack("", 0, 0)

        return result
