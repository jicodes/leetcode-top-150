from collections import deque
from typing import List


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        # If the end_word is not in the word_list, there is no possible transformation
        if end_word not in word_list:
            return 0

        # Convert word_list to a set for O(1) lookups
        word_set = set(word_list)

        # Initialize BFS queue with the begin_word and a length of 1
        queue = deque([(begin_word, 1)])

        # Set to keep track of visited words
        visited = set([begin_word])

        while queue:
            curr_word, length = queue.popleft()

            # Generate all possible transformations
            for i in range(len(curr_word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char != curr_word[i]:
                        next_word = curr_word[:i] + char + curr_word[i + 1 :]

                        # If the next word is the end_word, return the length
                        if next_word == end_word:
                            return length + 1

                        # If the next word is in the word_set and not visited
                        if next_word in word_set and next_word not in visited:
                            visited.add(next_word)
                            queue.append((next_word, length + 1))

        # If no valid transformation path found, return 0
        return 0


# Example usage:
# begin_word = "hit"
# end_word = "cog"
# word_list = ["hot","dot","dog","lot","log","cog"]
# sol = Solution()
# print(sol.ladderLength(begin_word, end_word, word_list))  # Output: 5
