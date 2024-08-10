class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to calculate x^n recursively
        def power(x: float, n: int) -> float:
            if n == 0:
                # Base case: any number raised to the power of 0 is 1
                return 1
            # Recursively calculate half = x^(n//2)
            half = power(x, n // 2)
            if n % 2 == 0:
                # If n is even, then x^n = (x^(n//2))^2
                return half * half
            else:
                # If n is odd, then x^n = (x^(n//2))^2 * x
                return half * half * x

        if n < 0:
            # If n is negative, calculate x^(-n) as 1/(x^n)
            x = 1 / x
            n = -n

        # Calculate x^n using the helper function
        return power(x, n)
