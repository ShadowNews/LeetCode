class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alf1 = {}
        alf2 = {}

        if len(s)!=len(t):
            return False

        else:
            for i in range(len(s)):
                s1 = s[i]
                s2 = t[i]
                if s1 in alf1 and alf1[s1] != s2:
                    return False
                if s2 in alf2 and alf2[s2] != s1:
                    return False
                alf1[s1] = s2
                alf2[s2] = s1
            return True
