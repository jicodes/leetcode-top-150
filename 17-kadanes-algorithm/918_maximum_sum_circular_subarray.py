from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Initialize variables to track the global max and min sums, current max and min sums, and total sum
        global_max, global_min = nums[0], nums[0]
        current_max, current_min = 0, 0
        total_sum = 0

        # Iterate through each number in the array
        for num in nums:
            # Update the current max sum
            current_max = max(current_max + num, num)
            # Update the current min sum
            current_min = min(current_min + num, num)
            # Add the current number to the total sum
            total_sum += num
            # Update the global max sum if the current max sum is greater
            global_max = max(global_max, current_max)
            # Update the global min sum if the current min sum is smaller
            global_min = min(global_min, current_min)

        # If all numbers are negative, global_max will be the maximum subarray sum
        # If not, return the maximum of global_max and the total sum minus the global min sum
        return max(global_max, total_sum - global_min) if global_max > 0 else global_max
