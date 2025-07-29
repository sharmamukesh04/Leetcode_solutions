class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        start, end, n = 0, len(matrix)-1, len(matrix)
        while start<end:
            for i in range(len(matrix[0])):
                matrix[start][i], matrix[end][i] = matrix[end][i], matrix[start][i]
            
            start+=1
            end-=1
        
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        