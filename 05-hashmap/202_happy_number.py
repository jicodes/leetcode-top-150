class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number: int) -> int:
            total_sum = 0
            while number > 0:
                digit = number % 10
                number = number // 10
                total_sum += digit * digit
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


# Example usage
solution = Solution()
print(solution.isHappy(19))  # Output: True
print(solution.isHappy(2))  # Output: False
