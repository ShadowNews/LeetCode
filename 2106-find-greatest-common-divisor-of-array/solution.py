class Solution(object):
    def findGCD(self, nums):
        a = min(nums)
        b = max(nums)
        while a!=0 and b!=0:
            if a>b:
                a = a%b
            else:
                b = b%a
        return a+b

        
