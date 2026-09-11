class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])

        top,bottom = 0,rows-1
        srow = [ ]
        while top<= bottom:
            mid = (top+bottom)//2
            row = matrix[mid]
            if row[0] > target:
                bottom = mid-1
            elif row[-1] < target:
                top = mid+1
            else:
                srow = row
                break
        left,right = 0,len(srow)-1

        while left<=right:
            mid = (left+right)//2
            if srow[mid] < target:
                left = mid+1
            elif srow[mid] > target:
                right = mid-1
            else:
                return True 
        return False