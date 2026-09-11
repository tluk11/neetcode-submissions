class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom = 0,len(matrix)-1
        row = 0 
        while top<= bottom:
            row = (top+bottom)//2
            if matrix[row][-1] < target:
                top = row+1
            elif matrix[row][0]> target:
                bottom = row-1
            else:
                break
        # row is found

        beg,end = 0,len(matrix[row])-1

        while beg<= end:
            mid = (beg+end)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                beg = mid+1
            else:
                end = mid-1
        return False