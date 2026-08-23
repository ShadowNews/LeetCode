class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for l in range(len(nums)):
            if nums[l] in seen:
                if l - seen[nums[l]] <= k:
                    return True
            seen[nums[l]] = l
        return False

        
