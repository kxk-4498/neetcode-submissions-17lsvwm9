class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        c=-1
        for i in range(len(matrix)):
            if  matrix[i][0]<=target<=matrix[i][-1]:
                c=i
        
        if c==-1:
            return False
        
        l=0
        h=len(matrix[i])

        while l<=h:
            m=(l+h)//2
            if target == matrix[c][m]:
                return True
            
            elif target > matrix[c][m]:
                l=m+1
            else:
                h=m-1
        
        return False