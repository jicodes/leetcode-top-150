from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Base case: if the input is empty, return an empty list
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # List to store the result combinations
        result = []

        # Backtracking function to generate combinations
        def backtrack(index, path):
            # If the path length is equal to the digits length, we have a complete combination
            if len(path) == len(digits):
                result.append("".join(path))
                return

            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            # Loop through the letters and recurse
            for letter in possible_letters:
                path.append(letter)  # Choose
                backtrack(index + 1, path)  # Explore
                path.pop()  # Un-choose

        # Initiate backtracking with an empty path and starting index of 0
        backtrack(0, [])

        return result
