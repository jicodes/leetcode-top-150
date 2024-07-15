from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check for an empty matrix
        if not matrix or not matrix[0]:
            return False

        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])
        # Initialize the binary search range
        left, right = 0, m * n - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index of the current range
            mid = left + (right - left) // 2
            # Convert the 1D mid index back to 2D coordinates
            mid_value = matrix[mid // n][mid % n]

            # Check if the mid value is the target
            if mid_value == target:
                return True
            # If target is greater, ignore the left half
            elif mid_value < target:
                left = mid + 1
            # If target is smaller, ignore the right half
            else:
                right = mid - 1

        # Target is not found in the matrix
        return False
