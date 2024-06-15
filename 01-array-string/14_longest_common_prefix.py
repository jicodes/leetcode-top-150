from typing import List


class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        # Initialize the result string
        ans = ""

        # If the list is empty, return an empty string
        if not v:
            return ans

        # Sort the list of strings
        v = sorted(v)

        # Take the first and the last string after sorting
        first = v[0]
        last = v[-1]

        # Compare characters of the first and last string
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]

        return ans


# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""
print(solution.longestCommonPrefix([""]))  # Output: ""
print(solution.longestCommonPrefix(["a"]))  # Output: "a"
