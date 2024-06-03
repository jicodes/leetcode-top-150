from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the total profit to 0
        total_profit = 0

        # Iterate over prices from the second element to the last
        for i in range(1, len(prices)):
            # If current price is higher than the previous price, add the difference to total profit
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]

        return total_profit
