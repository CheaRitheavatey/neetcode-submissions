class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)
        result = float('inf')

        while lower <= upper:
            output = 0
            mid = (lower+upper)//2
            for i in piles:
                num = math.ceil(i/mid)
                output +=num
            if output > h:
                lower = mid + 1
            elif output <= h:
                result = min(result,mid)
                upper = mid - 1
        return result
            

    # for all element inside piles
    # 1/mid = --
    # 4/mid = --
        
