class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        current_number = 0
        current_result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "+":
                current_result += sign * current_number
                current_number = 0
                sign = 1
            elif char == "-":
                current_result += sign * current_number
                current_number = 0
                sign = -1
            elif char == "(":
                # Push the current result and sign onto the stack
                stack.append(current_result)
                stack.append(sign)
                # Reset the current result and sign
                current_result = 0
                sign = 1
            elif char == ")":
                # Complete the current number calculation
                current_result += sign * current_number
                current_number = 0
                # Apply the sign before the parenthesis
                current_result *= stack.pop()
                # Add the result before the parenthesis
                current_result += stack.pop()
            # Ignore spaces

        # Add the last accumulated number
        if current_number != 0:
            current_result += sign * current_number

        return current_result


# Example usage
solution = Solution()
print(solution.calculate("1 + 1"))  # Output: 2
print(solution.calculate(" 2-1 + 2 "))  # Output: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
