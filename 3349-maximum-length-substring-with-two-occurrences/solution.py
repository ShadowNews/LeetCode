class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        frequence = {}
        l = 0
        res = 0
        for r in range(len(s)):
            frequence[s[r]] = frequence.get(s[r],0) + 1
            while frequence[s[r]] > 2:
                frequence[s[l]]-=1
                l += 1
                
            
            if r-l+1 > res:
                res = r-l+1
        return res
            

            
                
            
