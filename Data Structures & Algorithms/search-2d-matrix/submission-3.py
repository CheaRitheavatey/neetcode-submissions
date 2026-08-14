class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        l = 0
        r = (n_row * n_col)-1

        while l <=r: 
            m = (l+r)//2
            m_row = m //n_col
            m_col = m % n_col


            if matrix[m_row][m_col] == target:
                return True

            if matrix[m_row][m_col] > target:
                r = m - 1
            
            else:
                l = m + 1

        return False