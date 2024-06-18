from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t)
        window_counts = defaultdict(int)

        required = len(dict_t)
        formed = 0

        left, right = 0, 0
        min_len = float("inf")
        min_left = 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_len == float("inf") else s[min_left : min_left + min_len]


# Example usage:
sol = Solution()
result = sol.minWindow("ADOBECODEBANC", "ABC")
print(result)  # Output: "BANC"
