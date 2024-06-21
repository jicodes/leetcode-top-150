from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_to_index = {}  # Dictionary to store the most recent index of each number

        for i, num in enumerate(nums):
            if num in num_to_index:  # Check if we have seen this number before
                # If we have seen it before, check the difference in indices
                if i - num_to_index[num] <= k:
                    # If the difference is <= k, we found a valid pair
                    return True
            # Update the dictionary with the current index of the number
            num_to_index[num] = i

        return False  # No valid pair found within the required distance
