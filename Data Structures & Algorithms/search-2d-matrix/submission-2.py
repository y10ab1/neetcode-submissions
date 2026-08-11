class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search for row
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l)//2
            if matrix[mid][-1] >= target and matrix[mid-1][-1] < target:
                break
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid - 1

        row = mid
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l)//2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False