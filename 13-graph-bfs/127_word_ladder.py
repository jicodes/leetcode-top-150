from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the endWord is not in the wordList, there is no possible transformation
        if endWord not in wordList:
            return 0

        # Convert wordList to a set for O(1) lookups
        wordSet = set(wordList)

        # Initialize BFS queue with the beginWord and a length of 1
        queue = deque([(beginWord, 1)])

        # Set to keep track of visited words
        visited = set([beginWord])

        while queue:
            currentWord, length = queue.popleft()

            # Generate all possible transformations
            for i in range(len(currentWord)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char != currentWord[i]:
                        nextWord = currentWord[:i] + char + currentWord[i + 1 :]

                        # If the next word is the endWord, return the length
                        if nextWord == endWord:
                            return length + 1

                        # If the next word is in the wordSet and not visited
                        if nextWord in wordSet and nextWord not in visited:
                            visited.add(nextWord)
                            queue.append((nextWord, length + 1))

        # If no valid transformation path found, return 0
        return 0


# Example usage:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# sol = Solution()
# print(sol.ladderLength(beginWord, endWord, wordList))  # Output: 5
