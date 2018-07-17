public class Solution {
    public int[][] prettyPrint(int A) {
        int size = A * 2 - 1;
        int [][] result = new int[size][size];
        
        int count = 0;
        while (A >= 1) {
            // upper / lower
            for (int i=0 + count; i < result.length - count; i++){
                result[0 + count][i] = A;
                result[result.length - 1 - count][i] = A;
            }
            // left / right
            for (int i=0 + count; i < result.length - count; i++){
                result[i][0 + count] = A;
                result[i][result.length - 1 - count] = A;
            }
            count += 1;
            A -= 1;
        }
        
        return result;
    }
}