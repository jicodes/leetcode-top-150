class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Increment count if the last bit is 1
            n >>= 1  # Right shift n by 1 bit
        return count


# Example usage:
sol = Solution()
print(sol.hammingWeight(11))  # Output: 3, since 11 in binary is 1011
