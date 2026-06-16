class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int NROWS = matrix.length;
        int NCOLS = matrix[0].length;

        int top = 0;
        int bot = NROWS -1;
        while (top <= bot) {
            int mrow = (top + bot) / 2;

            if (target > matrix[mrow][NCOLS - 1]) {
                top = mrow + 1;
            } else if (target < matrix[mrow][0]) {
                bot = mrow - 1;
            } else break;
        }

        if ( top > bot ) return false;

        int row = (top + bot) /2;
        int l = 0, r = NCOLS-1;
        while (l <= r) {
            int m = (l + r) /2;

            if (target > matrix[row][m]) {
                l = m + 1;
            }

            else if (target < matrix[row][m]) {
                r = m - 1;
            } 
            
            else return true;
        }

        return false;
        
    }
}
