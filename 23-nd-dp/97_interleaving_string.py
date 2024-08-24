class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the total length of s1 and s2 doesn't match s3, return False
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize a DP table with False values
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        # Base case: empty s1 and s2 can form an empty s3
        dp[0][0] = True

        # Fill first column: s1[:i] should match s3[:i]
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        # Fill first row: s2[:j] should match s3[:j]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the DP table
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # Check if s1[i-1] matches s3[i+j-1] and dp[i-1][j] is True
                # Or if s2[j-1] matches s3[i+j-1] and dp[i][j-1] is True
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                )

        # Result is whether the entire s3 can be formed
        return dp[len(s1)][len(s2)]
