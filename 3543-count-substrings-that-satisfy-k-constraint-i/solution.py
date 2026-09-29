class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = 0
        zeroes = 0 
        once = 0
        ans = 0
        for r in range(len(s)):
            if s[r] == "1":
                once += 1
            if s[r] == "0":
                zeroes += 1
            while zeroes > k and once>k:
                if s[l] == "1":
                    once -= 1
                else:
                    zeroes -= 1
                l+=1
            ans += r-l+1
        return ans
            
