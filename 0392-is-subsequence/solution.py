class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        
        for p2 in range(len(t)):
            if p1 < len(s) and s[p1]==t[p2]:
                p1+=1
        return p1==len(s)
            


        
