class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l = 0

        for i in range(1,len(height)):
            maxLeft = max(height[:i])
            maxRight = max(height[i:])
            minHeight = min(maxLeft, maxRight)

            total += max(0, (minHeight - height[i]))

        return total



        