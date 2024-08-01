class Solution:
    def reverseBits(self, n: int) -> int:
        # Initialize result to 0
        result = 0
        # Iterate through all 32 bits of the input number
        for i in range(32):
            # Shift result left by 1 bit to make space for the next bit
            result <<= 1
            # Extract the least significant bit of n and add it to result
            result |= n & 1
            # Shift n right by 1 bit to process the next bit
            n >>= 1
        return result
