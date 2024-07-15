# kadane's algorithm
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current_sum and max_sum with the first element of the array
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update current_sum to be the maximum of the current element
            # or the sum of current_sum and the current element
            current_sum = max(num, current_sum + num)

            # Update max_sum to be the maximum of max_sum and current_sum
            max_sum = max(max_sum, current_sum)

        # Return the maximum sum of a contiguous subarray found
        return max_sum
