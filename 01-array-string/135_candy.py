from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        candies = [1] * n

        # Traverse from left to right, and make sure each child has more candies than the previous one if their rating is higher
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse from right to left, and make sure each child has more candies than the next one if their rating is higher
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # The total candies needed is the sum of all the candies in the list
        return sum(candies)
