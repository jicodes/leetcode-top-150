from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize the amount of gas (steps we can take) to 0
        gas = 0
        # Iterate over each number in the array
        for n in nums:
            # If we run out of gas before reaching this position, we can't proceed, so return False
            if gas < 0:
                return False
            # If the current number (amount of gas available at this position) is greater than our current gas,
            # we gas up our car (replace our current amount of gas with this new amount)
            elif n > gas:
                gas = n
            # Move to the next position, which costs 1 unit of gas
            gas -= 1

        # If we complete the loop, it means we can reach the last position, so return True
        return True
