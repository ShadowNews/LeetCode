class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # window = 0
        # for i in range(2):
        #     window += nums[i]

        # stack = []
        # stack.append(window)
        # l=0
        # for r in range(2,len(nums)):
        #     stack.append(window - nums[l]+nums[r])
        #     l+=1

        # frequence = {}
        # for i in stack:
        #     frequence[i] = frequence.get(i,0) + 1

        # res = 0
        # for j in stack:
        #     if frequence[j]%2==0:
        #         return True
        #     else:
        #         res = False
        # return res
        seen = set()
        for i in range(len(nums)-1):
            window = nums[i] + nums[i+1]

            if window in seen:
                return True
            seen.add(window)

        return False

        
        

        
        
