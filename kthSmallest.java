public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int kthsmallest(final int[] A, int B) {
        if (B == 1) {
            int min = Integer.MAX_VALUE;
            for (int i=0; i<A.length;i++) {
                if (A[i] < min) {
                    min = A[i];
                }
            }
            return min;
        }
        int [] mins = new int[B];
        for (int i=0;i<mins.length;i++){
            mins[i] = Integer.MAX_VALUE;
        }
        
        for (int i=0; i < A.length; i++) {
            if (A[i] < mins[mins.length-1]) {
                mins = checkCurrent(A[i], mins);
            }
        }
        
        return mins[mins.length-1];
    }
    
    public int[] checkCurrent(int toCheck, int[] mins) {
        if (toCheck < mins[0]) {
            int next;
            int curr = mins[0];
            mins[0] = toCheck;
            for (int i=1; i< mins.length-1;i++) {
                next = mins[i];
                mins[i] = curr;
                curr = next;
            }
        } else {
            int start = 0;
            while (mins[start] < toCheck) {
                start +=1;
            }
            int next;
            int curr = mins[start];
            mins[start] = toCheck;
            for (int i=start+1; i< mins.length;i++) {
                next = mins[i];
                mins[i] = curr;
                curr = next;
            }
        }
        return mins;
    }
}
