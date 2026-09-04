class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_char_nice(string):
            chars = set(string)

            for char in chars:
                if char.lower() not in chars or char.upper() not in chars:
                    return False

            return True

        best = ""

        for l in range(len(s)):
            for r in range(l, len(s)):
                window = s[l:r + 1]

                if is_char_nice(window):
                    if len(window) > len(best):
                        best = window

        return best
