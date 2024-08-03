class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for num in nums:
            single ^= num  # XOR the current number with the result
        return single


# Example usage
sol = Solution()
print(sol.singleNumber([4, 1, 2, 1, 2]))  # Output: 4
