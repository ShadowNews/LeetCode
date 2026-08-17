class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        for i in s:
            count[i] = count.get(i,0)+1   
        odd_count = 0 
        for freq in count.values():
            if freq % 2 !=0:
                odd_count += 1
        return odd_count <= 1


        
        
        
