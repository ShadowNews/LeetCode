class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: 
            return True
        else:
            s = s.lower()
            p1 = 0
            p2 = len(s)-1
            while p1<p2:
                if not s[p1].isalnum():
                    p1+=1
                    continue
                elif not s[p2].isalnum():
                    p2-=1
                    continue
                else:
                    if s[p1]==s[p2]:
                        p1+=1
                        p2-=1
                        continue   
                    else:
                        return False
            return True



