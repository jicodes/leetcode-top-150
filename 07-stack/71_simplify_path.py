class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path by '/'
        parts = path.split("/")

        # Stack to store the valid path parts
        stack = []

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)

        # Join the stack to form the simplified canonical path
        return "/" + "/".join(stack)


# Example usage
solution = Solution()
print(solution.simplifyPath("/home/"))  # Output: "/home"
print(solution.simplifyPath("/../"))  # Output: "/"
print(solution.simplifyPath("/home//foo/"))  # Output: "/home/foo"
print(solution.simplifyPath("/a/./b/../../c/"))  # Output: "/c"
print(solution.simplifyPath("/a/../../b/../c//.//"))  # Output: "/c"
print(solution.simplifyPath("/a//b////c/d//././/.."))  # Output: "/a/b/c"
