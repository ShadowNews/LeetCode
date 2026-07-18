def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums),min(nums))
        
