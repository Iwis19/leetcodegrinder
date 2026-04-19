class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # binary search practice

        # use the first value of each row to see which row its in

        # then use the first value in the row and the last value in the row to see if it is in or not


        """
        w double binary search

        1. should always have the "equals to target" case at the start as a good practice, and then edit high low values
        etc

        0 ms runtime beats 100
        """


        top, bottom = 0, len(matrix)-1
        row = 0

        while top <= bottom:

            mid = (top+bottom)//2

            # good
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            
            # too big -> bottom turns into mid
            elif matrix[mid][0] > target:
                bottom = mid - 1
            
            # too small -> top turns into mid
            elif matrix[mid][0] < target:
                top = mid + 1

        left, right = 0, len(matrix[row])-1

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            
            # too big
            elif matrix[row][mid] > target:
                right = mid - 1
            
            # too small
            elif matrix[row][mid] < target:
                left = mid + 1

        return False
