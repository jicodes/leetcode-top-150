class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are not the same, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create dictionaries to count the occurrences of each character
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Compare the two dictionaries
        return count_s == count_t


# Example usage
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # Output: True
print(solution.isAnagram("rat", "car"))  # Output: False
