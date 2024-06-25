class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # Stack to store operands
        stack = []

        # Define the operators
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),  # Use int() to truncate towards zero
        }

        for token in tokens:
            if token in operators:
                # Pop the last two operands
                b = stack.pop()
                a = stack.pop()
                # Perform the operation and push the result
                result = operators[token](a, b)
                stack.append(result)
            else:
                # Push the number onto the stack
                stack.append(int(token))

        # The result is the last element in the stack
        return stack[0]


# Example usage
solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
print(solution.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
print(
    solution.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )
)  # Output: 22
