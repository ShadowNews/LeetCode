class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        res = 0
        for i in nums:
            count[i] = count.get(i,0)+1
        

        for num in count:
            if num+1 in count:
                res = max(res,count[num] + count[num+1])
            
        # nums = sorted(nums)
        # l = 0
        # res = 0
        # for r in range(len(nums)):
        #     while nums[r]-nums[l]>1:
        #         l+=1
        #     if nums[r]-nums[l]==1:
        #         res = max(res,r-l+1)

        return res


