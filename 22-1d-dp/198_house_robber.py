from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev1 = 0  # This will hold the maximum money up to the previous house
        prev2 = 0  # This will hold the maximum money up to the house before the previous one

        for num in nums:
            curr = max(prev1, prev2 + num)  # Max money if we rob this house or not
            prev2 = prev1  # Update prev2 to be prev1
            prev1 = curr  # Update prev1 to be the current max

        return prev1
