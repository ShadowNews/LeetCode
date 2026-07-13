class Solution(object):
    def runningSum(self, nums):
        ans = [0]*len(nums)
        j = 0
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            ans[j] = sum
            j+=1
        return ans
        # new_array = []
        # new_array.append(nums[0])
        # for i in range(1,len(nums)):
        #     cursum = sum(nums[:i])
        #     new_array.append(cursum+nums[i])
        # return new_array

            

        
            




        
