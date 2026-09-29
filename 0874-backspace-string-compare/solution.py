class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for i in s:
            if i == "#":
                if len(stack_s)!=0:
                    stack_s.pop()
            else:
                stack_s.append(i)
        for j in t:
            if j == "#":
                if len(stack_t)!=0:
                    stack_t.pop()
            else:
                stack_t.append(j)
        
        return stack_s == stack_t
