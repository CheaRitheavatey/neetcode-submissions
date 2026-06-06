class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        count = 0
        # its the begining if i - 1 not in set
        for i in s:
            if i - 1 not in s:
                length = 1

                while i + length in s:
                    length+= 1
                count = max(count, length)
        return count
