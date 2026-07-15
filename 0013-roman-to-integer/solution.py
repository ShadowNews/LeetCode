translate = {"VI":6, "IV":4, "IX":9,"LX":40, "XC":90, "CD":400, "CM":900, "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "":0}


class Solution(object):
    def romanToInt(self, s):
        total = 0
        i = 0 
        while i<len(s):
            if i+1<len(s) and translate[s[i]]<translate[s[i+1]]:
                total += translate[s[i+1]] - translate[s[i]]
                i+=2
            else:
                total += translate[s[i]]
                i+=1
        return total

        
