from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables to keep track of jumps, the current end of the range, and the farthest point we can reach
        jumps = 0
        current_end = 0
        farthest = 0

        # Iterate over the array, but not including the last element
        for i in range(len(nums) - 1):
            # Update the farthest point we can reach
            farthest = max(farthest, i + nums[i])

            # If we have reached the end of the current range
            if i == current_end:
                # Update the end of the current range to the farthest point we can reach
                current_end = farthest
                # Increment the number of jumps
                jumps += 1

        return jumps
