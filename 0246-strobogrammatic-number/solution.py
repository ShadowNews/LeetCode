class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"}
        l = 0
        r = len(num)-1
        while l <= r:
            if num[l] in rotate:
                if rotate[num[l]] == num[r]:
                    l += 1
                    r-=1
                else: 
                    return False
            else: return False
        return True
