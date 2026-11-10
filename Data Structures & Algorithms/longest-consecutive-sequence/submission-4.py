class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count = 0
        for i in num_set:
            if i - 1 not in num_set:
                # nums[i] is the starting
                curr = 0
                val = i
                while val in num_set:
                    curr += 1
                    val += 1
                count = max(count, curr)
        return count

        