from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the string and join to use it as a key
            key = "".join(sorted(word))
            anagrams[key].append(word)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())


# Example usage
solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
