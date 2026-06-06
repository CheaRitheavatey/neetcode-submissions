class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 3:
            # + 4 -> return and break
            # + 5
            # + 6

        # 3 + 4 = 7 -> 7 - 3 = 4
        # store {4 : 0}
        # 3 -> check if index of 3 which 0 is in the dict then return current index and that index
        store = {}

        for i in range(len(nums)):
            if nums[i] in store.keys():
                return [store.get(nums[i]),i]
            s = target - nums[i]
            store[s] = i

        