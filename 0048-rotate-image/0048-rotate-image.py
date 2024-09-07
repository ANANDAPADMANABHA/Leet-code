class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
    
    # Step 1: Transpose the matrix using a single loop to avoid explicit nested loops
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row without a nested loop using list slicing
        for i in range(n):
            matrix[i] = matrix[i][::-1]  #
            
        return matrix