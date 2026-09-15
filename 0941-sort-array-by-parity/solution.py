class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        write = 0
        r = len(nums)-1
        while write < r:
            if nums[r]%2==0:
                nums[r],nums[write] = nums[write],nums[r]
                write += 1
            else: r-=1
        return nums
            

            
        return nums

