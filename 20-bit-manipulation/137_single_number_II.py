class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            twos |= ones & num  # Update bits that have appeared twice
            ones ^= num  # Update bits that have appeared once
            threes = ones & twos  # Calculate bits that have appeared three times
            ones &= ~threes  # Clear bits that have appeared three times from ones
            twos &= ~threes  # Clear bits that have appeared three times from twos
        return ones


# Example usage
# sol = Solution()
# print(sol.singleNumber([2, 2, 3, 2]))  # Output: 3
