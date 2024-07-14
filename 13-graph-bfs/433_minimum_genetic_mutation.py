from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # If the end gene is not in the bank, return -1 as it's impossible to reach
        if end not in bank:
            return -1

        # Convert the bank list to a set for O(1) lookups
        bank_set = set(bank)
        # Initialize the BFS queue with the start gene and 0 mutations
        queue = deque([(start, 0)])
        # Set to keep track of visited genes
        visited = set([start])

        # Perform BFS
        while queue:
            current_gene, mutations = queue.popleft()

            # If the current gene matches the end gene, return the mutation count
            if current_gene == end:
                return mutations

            # Generate all possible mutations by changing each character
            for i in range(len(current_gene)):
                for char in "ACGT":
                    if char != current_gene[i]:
                        # Create a new mutated gene
                        mutated_gene = current_gene[:i] + char + current_gene[i + 1 :]

                        # If the mutated gene is valid and not visited, add it to the queue
                        if mutated_gene in bank_set and mutated_gene not in visited:
                            visited.add(mutated_gene)
                            queue.append((mutated_gene, mutations + 1))

        # If no valid mutation path found, return -1
        return -1


# Example usage:
# start = "AACCGGTT"
# end = "AACCGGTA"
# bank = ["AACCGGTA"]
# sol = Solution()
# print(sol.minMutation(start, end, bank))  # Output: 1
