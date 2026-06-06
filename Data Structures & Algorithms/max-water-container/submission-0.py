class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxArea = -1
        while l < r:
            minHeight = min(heights[l], heights[r])
            width = len(heights[l:r])
            area = minHeight * width
            maxArea = max(maxArea, area)
            if heights[l] <= heights[r]:
                l+=1
            elif heights[l] > heights[r]:
                r-=1

        return maxArea