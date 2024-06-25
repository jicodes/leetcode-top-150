class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []

        # Dictionary to hold mappings of opening to closing brackets
        bracket_map = {"(": ")", "{": "}", "[": "]"}

        for char in s:
            # If the character is an opening bracket
            if char in bracket_map:
                # Push it onto the stack
                stack.append(char)
            else:
                # If it's a closing bracket, check the stack
                if not stack or bracket_map[stack.pop()] != char:
                    return False

        # If the stack is empty, all brackets are closed properly
        return not stack


# Example usage
solution = Solution()
print(solution.isValid("()"))  # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))  # Output: False
print(solution.isValid("([)]"))  # Output: False
print(solution.isValid("{[]}"))  # Output: True
