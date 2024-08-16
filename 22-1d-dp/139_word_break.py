from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert the wordDict to a set for O(1) lookups
        word_set = set(wordDict)

        # dp[i] will be True if the substring s[0:i] can be segmented into words in wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case: an empty string can always be segmented

        # Fill the dp array
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[0:j] can be segmented and s[j:i] is in the wordDict
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further if dp[i] is already True

        # The last element in dp will be True if s can be segmented
        return dp[len(s)]
