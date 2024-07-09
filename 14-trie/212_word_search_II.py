from typing import List, Set


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # To store the complete word at the end node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.word = word  # Store the word at the end node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Construct the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # Step 2: Initialize variables
        self.result = set()  # Use a set to avoid duplicates
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        # Step 3: Perform DFS from each cell
        for r in range(self.rows):
            for c in range(self.cols):
                self.dfs(trie.root, r, c)

        return list(self.result)

    def dfs(self, node: TrieNode, r: int, c: int) -> None:
        char = self.board[r][c]
        if char not in node.children:
            return

        next_node = node.children[char]

        if next_node.word:
            self.result.add(next_node.word)

        # Mark the cell as visited by replacing it with '#'
        self.board[r][c] = "#"

        # Explore neighbors
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < self.rows
                and 0 <= nc < self.cols
                and self.board[nr][nc] != "#"
            ):
                self.dfs(next_node, nr, nc)

        # Restore the cell's original value
        self.board[r][c] = char


# Example usage:
# board = [
#     ["o", "a", "a", "n"],
#     ["e", "t", "a", "e"],
#     ["i", "h", "k", "r"],
#     ["i", "f", "l", "v"]
# ]
# words = ["oath", "pea", "eat", "rain"]
# sol = Solution()
# print(sol.findWords(board, words))  # Output: ["oath", "eat"]
