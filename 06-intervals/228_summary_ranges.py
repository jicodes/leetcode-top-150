from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []  # List to store the resulting intervals
        n = len(nums)
        if n == 0:
            return ranges

        start = nums[0]  # Initialize the start of the current interval

        for i in range(1, n):
            # Check if the current number is not consecutive to the previous one
            if nums[i] != nums[i - 1] + 1:
                # If the start is the same as the previous number, it's a single number interval
                if start == nums[i - 1]:
                    ranges.append(str(start))
                else:
                    # Otherwise, it's a range from start to the previous number
                    ranges.append(f"{start}->{nums[i-1]}")
                start = nums[i]  # Start a new interval with the current number

        # Handle the last interval
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(f"{start}->{nums[-1]}")

        return ranges
