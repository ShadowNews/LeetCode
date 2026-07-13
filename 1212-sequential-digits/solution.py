class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []
        string = "123456789"
        for i in range(len(string)):
            for j in range(1+i,len(string)+1):
                test_str = int(string[:j][i:])
                if low <= test_str <= high:
                    ans.append(test_str)    
        return sorted(ans)
         
