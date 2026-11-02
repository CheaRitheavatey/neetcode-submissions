class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_num = {}
        for i in range(len(nums)):
            number = target - nums[i]
            if number not in set_num:
                set_num[nums[i]] = i 
            else:
                return [set_num[number], i]
