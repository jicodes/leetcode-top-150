class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Square root of 0 or 1 is the number itself.

        left, right = 2, x // 2  # Start search between 2 and x // 2.

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid  # Exact square root found.
            elif square < x:
                left = mid + 1  # Search in the higher half.
            else:
                right = mid - 1  # Search in the lower half.

        return right  # Return the integer part of the square root.
