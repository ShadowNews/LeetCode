class Solution:
    def twoSum(self, nums, target):
        lookup = {}

        for i, num in enumerate(nums):
            answer = target - num

            if answer in lookup:
                return [lookup[answer], i]

            lookup[num] = i
