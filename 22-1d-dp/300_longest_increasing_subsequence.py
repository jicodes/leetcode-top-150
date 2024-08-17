class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)  # Initialize dp array, each element starts with a subsequence of length 1
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # Check if the subsequence can be extended
                    dp[i] = max(dp[i], dp[j] + 1)  # Update dp[i] with the longest subsequence ending at i
        
        return max(dp)  # Return the length of the longest increasing subsequence
