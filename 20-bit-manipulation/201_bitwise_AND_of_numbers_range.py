class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift_count = 0
        # Shift left and right until they are the same
        while left != right:
            left >>= 1
            right >>= 1
            shift_count += 1
        # Shift the common prefix back to its original position
        return left << shift_count


# Example usage
# sol = Solution()
# print(sol.rangeBitwiseAnd(5, 7))  # Output: 4
