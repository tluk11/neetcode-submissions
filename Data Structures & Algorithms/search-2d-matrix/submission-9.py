class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        left,right = 0,len(matrix[0])-1
        row = -1
        while top<= bottom:
            mid = (top+bottom)//2
            if matrix[mid][0] > target:
                bottom = mid-1
            elif matrix[mid][right] < target:
                top = mid+1
            else:
                row = mid
                break
        if row == -1:
            return False

        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid] > target:
                right = mid-1
            elif matrix[row][mid] < target:
                left = mid+1
            else:
                return True
        return False
