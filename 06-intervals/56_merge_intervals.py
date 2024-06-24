from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = []

        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval does not overlap with the previous one
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, so merge the current and previous intervals
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# Example usage:
solution = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution.merge(intervals))  # Output: [[1, 6], [8, 10], [15, 18]]
