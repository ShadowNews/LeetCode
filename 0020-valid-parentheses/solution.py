class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "}":"{",
            ")":"(",
            "]":"["}
        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] != pairs[char]:
                        return False
                    else: stack.pop()
                
        return not stack





