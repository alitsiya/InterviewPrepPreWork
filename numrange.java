public static int numRange(int[] A, int B, int C) {
    if (A.length == 0) {
        return 0;
    }
    int res = 0;
    int currSum = 0;
    for (int i=0; i< A.length; i++) {
        System.out.println("Checking chains for " + i);
        currSum = A[i];
        int start = i;
        while (true) {
            System.out.println("checking from " + i + " till " + start + ": " + A[i] + ".."+A[start] + ", sum: " + currSum);
            if (currSum >= B && currSum <= C && start < A.length-1) {
                currSum += A[start+1];
                start += 1;
                res += 1;
            } else if (currSum < B && start < A.length-1) {
                currSum += A[start+1];
                start += 1;
            } else {
                if (currSum >= B && currSum <= C) {
                    res +=1;
                }
                System.out.println("result: " + res + ", sum: "+ currSum);
                break;
            }
        }
    }
    return res;
}