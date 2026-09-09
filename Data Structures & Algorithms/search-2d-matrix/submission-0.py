class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1

        # find a valid row that could contain this number
        while top <= bottom:
            mid = (top + bottom) // 2
            # if the last number of the current row < target, then you gotta move 
            # down to the next possible row
            if matrix[mid][-1] < target:
                top = mid + 1
            # if the last number of the current row > target, then you gotta move 
            # up to the next possible row
            elif matrix[mid][0] > target:
                bottom = mid - 1
            # found a valid row
            else:
                break
        
        # if no valid row is found
        if not (top <= bottom):
            return False
        
        row = (top + bottom) // 2
        left, right = 0, cols - 1
        
        # this is just classic 1d array binary search
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] < target:
                left = mid + 1
            else: 
                return True
        
        return False
        
        