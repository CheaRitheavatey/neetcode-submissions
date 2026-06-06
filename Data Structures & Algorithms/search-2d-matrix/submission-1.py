import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = np.array(matrix)
        flat = arr.flatten()

        for i in flat:
            if target == i: return True

        return False
