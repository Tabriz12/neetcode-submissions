class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


        r_min = 0
        r_max = len(matrix)-1

        r = -1

        while r_min <= r_max:

            mid = (r_min+r_max) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:

                r = mid

                r_min = len(matrix)
            
            elif matrix[mid][0] > target:

                r_max = mid - 1

                
            
            elif matrix[mid][-1] < target:

                r_min = mid + 1
            
        
        if r == -1:
            return False
        

        c_min = 0
        arr = matrix[r]
        c_max = len(arr)-1

        while c_min <= c_max:

            mid = (c_min+c_max) // 2

            if arr[mid] == target:

                return True
            
            elif arr[mid] > target:

                c_max = mid - 1
            
            else:

                c_min = mid + 1
        
        return False











        