class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        window = 0
        l = 0
        res = nums[l+k-1] - nums[l]
        while l+k-1 < len(nums): 
            window = nums[l+k-1] - nums[l]
            if window < res:
                res = window
            l+=1
        return res

