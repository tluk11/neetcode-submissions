class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        bottom, top = 0, len(matrix) - 1
        end = len(matrix[0]) - 1
        
        # Binary search for the correct row
        while bottom <= top:
            mid = (bottom + top) // 2
            if matrix[mid][0] > target:
                top = mid - 1
            elif matrix[mid][end] < target:
                bottom = mid + 1
            else:
                break
        else:
            return False  # No valid row found

        row = mid

        # Binary search within the row
        left, right = 0, end
        while left <= right:
            mid2 = (left + right) // 2
            if matrix[row][mid2] < target:
                left = mid2 + 1
            elif matrix[row][mid2] > target:
                right = mid2 - 1
            else:
                return True  # matrix[row][mid2] == target

        return False  # Target not found in the row
