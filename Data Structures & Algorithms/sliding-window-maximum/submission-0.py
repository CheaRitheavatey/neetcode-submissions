class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        result = []
        for r in range(k,len(nums)+1):
            max_num = max(nums[l:r])
            result.append(max_num)
            l+=1
        return result

        