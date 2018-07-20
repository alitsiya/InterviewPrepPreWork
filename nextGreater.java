public int[] nextGreater(int[] A) {
    int[] B = new int[A.length];
    for (int i=0;i<B.length;i++) {
        B[i] = -1;
    }
    for (int i=0; i< A.length-1; i++) {
        int curr = A[i];
        for (int j=i+1; j<A.length; j++) {
            if (A[j] > curr) {
                B[i] = A[j];
                break;
            }
        }
    }
    return B;
}