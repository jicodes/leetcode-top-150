class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        # Dictionaries to keep track of the mapping from pattern to words and words to pattern
        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, words):
            # If there's an existing mapping for the pattern character, it must match the word
            if p in pattern_to_word:
                if pattern_to_word[p] != w:
                    return False
            # If there's an existing mapping for the word, it must match the pattern character
            if w in word_to_pattern:
                if word_to_pattern[w] != p:
                    return False

            # Create the new mappings
            pattern_to_word[p] = w
            word_to_pattern[w] = p

        return True
