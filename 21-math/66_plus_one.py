class Solution:
    def plusOne(self, digits):
        n = len(digits)

        # Traverse the digits array from the end to the start
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, simply increment it and return the list
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set the current digit to 0 and move to the next digit
            digits[i] = 0

        # If all digits were 9, we have a carry over and need to add a leading 1
        return [1] + digits


# Example usage:
sol = Solution()
print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(sol.plusOne([9, 9, 9]))  # Output: [1, 0, 0, 0]
