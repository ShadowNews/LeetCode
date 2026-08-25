class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hz = 0

        for i in range(len(nums)+1):
            hz += i
        return hz - sum(nums)

            

