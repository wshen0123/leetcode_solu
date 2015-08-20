class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        firstCol = False
        if 0 in [matrix[r][0] for r in range(m)]:
            firstCol = True
        
        for c in range(1, n):
            currCol = False
            for r in range(m):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    currCol = True
            if currCol:
                for r in range(m):
                    matrix[r][c] = 0
        
        #clear entire rows with 0
        for r in range(m):
            if matrix[r][0] == 0:
                matrix[r] = [0] * n
        
        #clear first col
        if firstCol:
            for r in range(m):
                matrix[r][0] = 0
        
        
        
