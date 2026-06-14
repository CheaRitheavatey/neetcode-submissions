import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = np.concatenate([nums1,nums2])
        arr = np.sort(arr,axis=None)
        # print(arr)

        if len(arr) % 2 == 0:
            # even arr length
            mid = len(arr)//2
            median = (arr[mid-1] + arr[mid])/2
            # print(median)
            return float(median)

        elif len(arr) % 2 != 0:
            # odd length
            mid = len(arr)//2
            # print(mid)
            return float(arr[mid])
                

        