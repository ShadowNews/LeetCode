def f(x):
    total = 0
    while x != 0:
        digit = x % 10
        total += digit ** 2
        x //= 10
    return total

class Solution:
    def isHappy(self, n: int) -> bool:
        already = set()
        while n!=1:
            if n in already:
                return False 
            already.add(n)
            n = f(n)
        return True


        
