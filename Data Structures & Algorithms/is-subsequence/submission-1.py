class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # matched s[i], move to next s character
            j += 1      # always advance pointer in t
        return i == len(s)
