class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cur = -1
        for fast in range(len(haystack)):
            if haystack[fast:fast+len(needle)] == needle:
                cur = fast
                return cur
        return cur
        
