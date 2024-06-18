from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Frequency count of characters in t
        char_count_t = Counter(t)
        window_counts = defaultdict(int)

        # Number of unique characters in t that need to be present in the window with required frequency
        total_required_chars = len(char_count_t)
        # Number of unique characters in the current window that match the required frequency in t
        valid_char_count = 0

        left, right = 0, 0
        min_len = float("inf")
        min_left = 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # Check if the current character added satisfies the frequency required
            if char in char_count_t and window_counts[char] == char_count_t[char]:
                valid_char_count += 1

            # Try and contract the window till the point where it ceases to be 'valid'
            while left <= right and valid_char_count == total_required_chars:
                char = s[left]

                # Save the smallest window until now
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[char] -= 1
                if char in char_count_t and window_counts[char] < char_count_t[char]:
                    valid_char_count -= 1

                left += 1

            right += 1

        return "" if min_len == float("inf") else s[min_left : min_left + min_len]


# Example usage:
sol = Solution()
result = sol.minWindow("ADOBECODEBANC", "ABC")
print(result)  # Output: "BANC"
