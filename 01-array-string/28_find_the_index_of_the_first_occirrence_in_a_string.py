class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is an empty string, return 0
        if not needle:
            return 0

        # If the length of haystack is less than the length of needle, return -1
        if len(haystack) < len(needle):
            return -1

        # Loop through the haystack and check for the needle
        for i in range(len(haystack) - len(needle) + 1):
            # If the substring of haystack from i to i+len(needle) matches needle, return i
            if haystack[i : i + len(needle)] == needle:
                return i

        # If needle is not found in haystack, return -1
        return -1


# Example usage:
solution = Solution()
print(solution.strStr("hello", "ll"))  # Output: 2
print(solution.strStr("aaaaa", "bba"))  # Output: -1
print(solution.strStr("", ""))  # Output: 0
print(solution.strStr("abc", "c"))  # Output: 2
print(solution.strStr("mississippi", "issip"))  # Output: 4
