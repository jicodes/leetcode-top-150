from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Sort the balloons by their ending coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for start, end in points:
            if start > current_end:
                arrows += 1
                current_end = end

        return arrows


# Example usage:
solution = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(solution.findMinArrowShots(points))  # Output: 2
