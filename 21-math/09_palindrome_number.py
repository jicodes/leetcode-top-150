class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            # Append the last digit of x to reversed_half
            reversed_half = reversed_half * 10 + x % 10
            # Remove the last digit from x by integer division
            x //= 10

        # Check if the number is a palindrome
        return x == reversed_half or x == reversed_half // 10


# Example usage:
sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121))  # Output: False
print(sol.isPalindrome(10))  # Output: False
