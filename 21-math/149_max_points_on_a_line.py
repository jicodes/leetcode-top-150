from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # If there are 2 or fewer points, all points are on the same line
        if len(points) <= 2:
            return len(points)

        def slope(p1, p2):
            """Calculate the slope between two points."""
            x1, y1 = p1
            x2, y2 = p2
            dx = x2 - x1
            dy = y2 - y1
            # Handle vertical lines
            if dx == 0:
                return float("inf")
            # Handle horizontal lines
            if dy == 0:
                return 0
            # Reduce the fraction to avoid floating point errors
            g = gcd(dx, dy)
            return (dy // g, dx // g)

        max_points = 0
        # Iterate through all points as potential line pivots
        for i, p1 in enumerate(points):
            # Dictionary to store slope: count of points
            slopes = defaultdict(int)
            for j, p2 in enumerate(points):
                # Skip the point itself
                if i != j:
                    # Calculate slope and increment count
                    s = slope(p1, p2)
                    slopes[s] += 1
            # Find the maximum number of points on a line with this pivot
            # Add 1 to include the pivot point itself
            current_max = max(slopes.values()) + 1 if slopes else 1
            # Update the overall maximum
            max_points = max(max_points, current_max)

        return max_points
