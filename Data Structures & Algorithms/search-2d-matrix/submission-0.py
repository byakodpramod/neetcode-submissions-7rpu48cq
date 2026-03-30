class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot=0,len(matrix)-1
        while top<=bot:
            mid = top + (bot-top)//2
            if target > matrix[mid][-1]:
                top = mid+1
            elif target < matrix[mid][0]:
                bot = mid-1
            else:
                break
        row = top + (bot-top)//2
        l,r=0,len(matrix[mid])-1
        while l<=r:
            mid = l+(r-l)//2
            if matrix[row][mid] < target:
                l = mid+1
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                return True
        return False