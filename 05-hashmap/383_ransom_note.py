class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            # replacing the first occurrence of the string char
            # in the string magazine with an empty string "".
            magazine = magazine.replace(char, "", 1)
        return True
