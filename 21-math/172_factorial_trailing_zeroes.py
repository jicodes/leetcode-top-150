class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        # Continue dividing n by 5 and add the quotient to count
        while n > 0:
            n //= 5  # Divide n by 5 to count multiples of 5, 25, 125, etc.
            count += n  # Add the result to count
        return count  # The total count will be the number of trailing zeroes
