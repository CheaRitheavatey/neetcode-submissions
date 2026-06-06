class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        store = {}
        p, l, r = 0, 1, len(nums) - 1  # l starts at 1 (just after p)

        while p < len(nums) - 2:
            store[nums[p]] = p
            
            # If the search pointers cross, advance anchor p and reset pointers
            if l >= r:
                p += 1
                l = p + 1          # l always resets to the right of p
                r = len(nums) - 1   # r resets to the very end
                continue

            # Your original checking logic
            if nums[l] + nums[r] == -nums[p]:
                triplet = [nums[p], nums[l], nums[r]]
                if triplet not in result:  # Simple check to prevent duplicate answers
                    result.append(triplet)
                l += 1  # FIX: Move l inward
                r -= 1  # FIX: Move r inward
                
            elif nums[l] + nums[r] < -nums[p]:
                l += 1
                
            elif nums[l] + nums[r] > -nums[p]:
                r -= 1

        print(result)
        return result
