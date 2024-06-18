class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = max_length = 0
        seen = {}

        for end, char in enumerate(s):
            # Check if the character char has been seen before and its last occurrence
            # is within the current window (i.e., at or after start).
            if seen.get(char, -1) >= start:
                start = seen[char] + 1  # Adjust the start of the window
            seen[char] = end  # Record the index of the current character
            max_length = max(max_length, end - start + 1)  # Update the maximum length

        return max_length
