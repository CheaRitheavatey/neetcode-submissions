class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        suffix = 1
        for i in range(len(nums)):
            output[i] = suffix
            suffix *= nums[i]
        
        prefix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= prefix
            prefix *= nums[i]
        
        return output
        