class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for word in words:
            letters = set(word.lower())
            if letters<=row1 or letters<=row2 or letters<=row3:
                res.append(word)
        return res

