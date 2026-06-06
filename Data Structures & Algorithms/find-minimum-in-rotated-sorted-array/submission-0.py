class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l<r:
            mid = l + (r-l)//2
            # print(mid)

            if nums[mid] > nums[r]:
                l = mid + 1
                # print("nums[l] = ", nums[l])
            else:
                r = mid
                # print("nums[r] = ", nums[r])
        return nums[l]
        