from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # If k >= n // 2, it's equivalent to the unlimited transactions problem
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        # DP table
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]
            for i in range(1, n):
                dp[t][i] = max(dp[t][i - 1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[t - 1][i] - prices[i])

        return dp[k][n - 1]
