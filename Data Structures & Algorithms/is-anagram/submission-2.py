class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            remaining = counts.get(char, 0)
            if remaining == 0:
                return False
            counts[char] = remaining - 1

        return True