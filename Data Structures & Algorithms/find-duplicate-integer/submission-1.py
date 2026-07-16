from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = Counter(nums)
        for num, count in store.items():
            if count > 1:
                return num

        

        