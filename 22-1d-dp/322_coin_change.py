from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize an array to store minimum number of coins for each amount
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0  # Minimum coins needed to make amount 0 is 0

        # Iterate through each coin denomination
        for coin in coins:
            # Update the minimum number of coins for each amount
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # Check if the final amount can be made with the given coins
        return dp[amount] if dp[amount] != float("inf") else -1
