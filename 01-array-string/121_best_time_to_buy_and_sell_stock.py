from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the minimum price to a very high value and max profit to 0
        min_price = float("inf")
        max_profit = 0

        # Iterate over each price in the list
        for price in prices:
            # Update the minimum price if the current price is lower
            if price < min_price:
                min_price = price
            # Calculate the profit if sold at current price and update max profit if higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
