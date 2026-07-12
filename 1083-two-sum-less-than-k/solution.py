class Solution(object):
    def twoSumLessThanK(self, nums, k):
        n = len(nums)
        l,r = 0, n-1
        nums.sort()
        res = -1
        while l<r:
            CurSum = nums[l] + nums[r]
            if CurSum < k:
                res = max(res,CurSum)
                l+=1
            else:
                r-=1
        return res




        
