from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        # Initialize a counts array of size n+1 to count the number of papers with each citation count
        counts = [0] * (n + 1)

        # Count citations
        for c in citations:
            # If the citation count is greater than or equal to n, count it as n
            if c >= n:
                counts[n] += 1
            else:
                counts[c] += 1

        # Calculate H-Index
        total = 0
        # Iterate from the end of the counts array to the beginning
        for i in range(n, -1, -1):
            # Add the number of papers with i citations to the total count
            total += counts[i]
            # If the total number of papers with at least i citations is greater than or equal to i
            if total >= i:
                return i

        # If no valid H-Index is found, return 0
        return 0
