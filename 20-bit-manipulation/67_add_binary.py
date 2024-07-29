class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Initialize the result string and carry
        result = []
        carry = 0

        # Pointers for both strings starting from the end
        i, j = len(a) - 1, len(b) - 1

        # Iterate while there are bits to process or carry is non-zero
        while i >= 0 or j >= 0 or carry:
            # Get the current bits from a and b, or 0 if out of bounds
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum of the bits and carry
            total = bit_a + bit_b + carry

            # Append the result of the current bit to result
            result.append(str(total % 2))

            # Update the carry
            carry = total // 2

            # Move to the next bit
            i -= 1
            j -= 1

        # Reverse the result and join to form the final binary string
        return "".join(reversed(result))


# Example usage:
# sol = Solution()
# print(sol.addBinary("11", "1"))  # Output: "100"
