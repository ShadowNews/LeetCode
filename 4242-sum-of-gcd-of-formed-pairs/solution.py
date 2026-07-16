def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_zn = 0
        prefix_gcd = []
        for i in nums:
            if i > max_zn:
                max_zn = i
            prefix_gcd.append(gcd(i,max_zn))
        prefix_gcd = sorted(prefix_gcd)
        summ = 0
        l = 0
        r = len(prefix_gcd)-1
        while l < r:
            summ += gcd(prefix_gcd[l],prefix_gcd[r])
            l+=1
            r-=1
        
        return summ
