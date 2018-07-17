public int longestConsecutive(final int[] A) {
        
        HashMap<Integer, Integer> d = new HashMap<>();

        for (int i=0;i<A.length; i++) {
            if (!d.containsKey(A[i])) {
                d.put(A[i], 1);
            }
        }

        int longest = 0;

        for (int i=0;i<A.length;i++) {
            if (d.containsKey(A[i])) {
                d.remove(A[i]);
                int res = 0;
                int up = A[i]+1;
                while (true) {
                    if (d.containsKey(up)) {
                        d.remove(up);
                        res += 1;
                        up += 1;
                    } else {
                        if (res > longest) {
                            longest = res;
                        }
                        break;
                    }
                }
                int down = A[i]-1;
                while (true) {
                    if (d.containsKey(down)) {
                        d.remove(down);
                        res += 1;
                        down -= 1;
                    } else {
                        if (res > longest) {
                            longest = res;
                        }
                        break;
                    }
                }
            }
        }
        return longest+1;
    }