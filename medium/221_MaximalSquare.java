class Solution {
    public int cache (int xPos, int yPos, int[][] matrix)
    {
        if(xPos + 1 < matrix.length
            && yPos + 1 < matrix[0].length
            && matrix[xPos][yPos] >= 1 
            && matrix[xPos + 1][yPos] >= 1
            && matrix[xPos][yPos + 1] >= 1
            && matrix[xPos + 1][yPos + 1] >= 1)
           return (1 + Math.min(
            Math.min(matrix[xPos + 1][yPos],matrix[xPos][yPos + 1]), matrix[xPos + 1][yPos + 1])
            );
        else if(matrix[xPos][yPos] == 1)
            return 1;
        return 0;
    }
    public int maximalSquare(char[][] matrix) {
       
       //convert char matrix into int matrix
       int[][] matrix1 = new int[matrix.length][matrix[0].length];
       for(int i = 0; i < matrix.length; i++)
       {
            for(int j = 0; j < matrix[0].length; j++)
            {
                if(matrix[i][j] == '1')
                    matrix1[i][j] = 1;
                else
                    matrix1[i][j] = 0;
            }
       }

       //find the largest square side length
       int ans = 0;
       for(int i = matrix.length - 1; i >= 0; i--)
       {
            for(int j = matrix[0].length - 1; j >= 0; j--)
            {
                 matrix1[i][j] = cache(i, j, matrix1);
                 ans = Math.max(matrix1[i][j], ans);
            }
       }
       return ans * ans;
    }
}
