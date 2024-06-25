class MinStack:
    def __init__(self):
        # Stack to store all elements
        self.stack = []
        # Stack to store minimum elements
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # If min_stack is empty or x is the new minimum, push it onto min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.stack:
            top_element = self.stack.pop()
            # If the popped element is the minimum, pop it from min_stack too
            if top_element == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element from the main stack
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top element from the min stack, which is the minimum element
        return self.min_stack[-1] if self.min_stack else None

# Example usage
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin()) # Output: -3
minStack.pop()
print(minStack.top())    # Output: 0
print(minStack.getMin()) # Output: -2
