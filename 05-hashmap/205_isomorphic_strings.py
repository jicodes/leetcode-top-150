class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Dictionaries to keep track of the mapping from s to t and t to s
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # If there's an existing mapping for char_s, it must match char_t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            # If there's an existing mapping for char_t, it must match char_s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False

            # Create the new mappings
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
