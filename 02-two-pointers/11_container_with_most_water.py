from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the width and the area
            width = right - left
            curr_area = min(height[left], height[right]) * width
            # Update max_area if the calculated current area is larger
            max_area = max(max_area, curr_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
