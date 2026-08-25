class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        window = 0
        for i in range(k):
            window += nums[i]
        best = window
        
        for right in range(k,len(nums)):
            window += nums[right]
            window -= nums[right - k]
            best = max(best,window)  
        return best/k

