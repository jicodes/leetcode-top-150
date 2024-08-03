class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            # Step 3: Update twos
            twos |= ones & num

            # Step 4: Update ones
            ones ^= num

            # Step 5: Calculate threes
            threes = ones & twos

            # Step 6: Remove threes from ones and twos
            ones &= ~threes
            twos &= ~threes

        return ones


# Example usage
sol = Solution()
print(sol.singleNumber([2, 2, 3, 2]))  # Output: 3
