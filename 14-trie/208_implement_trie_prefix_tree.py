class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children and a boolean to mark the end of a word
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        # The root of the Trie is an empty node
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start from the root node
        curr = self.root
        for char in word:
            # If the character is not in the current node's children, add it
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Move to the child node
            curr = curr.children[char]
        # After inserting all characters, mark the end of the word
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Start from the root node
        curr = self.root
        for char in word:
            # If the character is not found, the word does not exist in the Trie
            if char not in curr.children:
                return False
            # Move to the child node
            curr = curr.children[char]
        # Check if the current node marks the end of the word
        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        # Start from the root node
        curr = self.root
        for char in prefix:
            # If the character is not found, no word with this prefix exists in the Trie
            if char not in curr.children:
                return False
            # Move to the child node
            curr = curr.children[char]
        # If we successfully traverse the prefix, return True
        return True


# Example usage:
# trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))   # Output: True
# print(trie.search("app"))     # Output: False
# print(trie.starts_with("app")) # Output: True
# trie.insert("app")
# print(trie.search("app"))     # Output: True
