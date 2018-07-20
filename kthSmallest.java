public int kthsmallest(final int[] A, int B) {
    int[] M = Arrays.copyOf(A, A.length);
    Arrays.sort(M);
    return M[B-1];
}