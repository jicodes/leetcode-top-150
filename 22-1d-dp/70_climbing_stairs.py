class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n  # Base cases: 1 way to climb 1 step, 2 ways to climb 2 steps

        first, second = 1, 2  # Initial values for 1 and 2 steps
        for i in range(3, n + 1):
            curr = first + second  # Calculate ways to climb 'i' steps
            first = second  # Update first to second
            second = curr  # Update second to current

        return second  # Return the total ways to climb 'n' steps
