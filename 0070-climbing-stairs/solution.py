cache = {}

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1

    if (a, b) in cache:
        return cache[(a, b)]

    result = f(a + 1, b) + f(a + 2, b)
    cache[(a, b)] = result

    return result

class Solution:
    def climbStairs(self, n: int) -> int:
        return f(0,n)
        
