from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        max_transactions = 2
        dp = [[0] * n for _ in range(max_transactions + 1)]

        for k in range(1, max_transactions + 1):
            max_diff = -prices[
                0
            ]  # Initialize max_diff to track the maximum of (dp[k-1][j] - prices[j])

            for i in range(1, n):
                # Update dp[k][i] with the max profit on day i with k transactions
                dp[k][i] = max(dp[k][i - 1], prices[i] + max_diff)

                # Update max_diff to ensure it holds the max value of (dp[k-1][i] - prices[i])
                max_diff = max(max_diff, dp[k - 1][i] - prices[i])

        # The maximum profit with at most 2 transactions up to the last day
        return dp[max_transactions][n - 1]
