from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0

        for word in words:
            # Check if adding the next word would exceed the maxWidth
            if current_length + len(current_line) + len(word) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - current_length):
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                result.append("".join(current_line))
                current_line, current_length = [], 0

            # Add the word to the current line
            current_line.append(word)
            current_length += len(word)

        # Last line - left justified
        result.append(" ".join(current_line).ljust(maxWidth))
        return result


# Example usage:
solution = Solution()
print(
    solution.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    )
)
print(solution.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(
    solution.fullJustify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    )
)
