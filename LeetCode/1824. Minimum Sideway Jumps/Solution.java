class Solution {
    public int minSideJumps(int[] obstacles) {
        // Time and Space Complexity: O(N)

        int INF = 1000000;
        int[][][] solutions = new int[obstacles.length][2][3];

        for (int i = 0; i < obstacles.length; i++) {
            for (int j = 0; j < 2; j++) {
                // last position requires
                // no sideway jump
                if (i == solutions.length - 1)
                    Arrays.fill(solutions[i][j], 0);
                else
                    Arrays.fill(solutions[i][j], INF);
            }
        }

        for (int pos = obstacles.length - 2; pos >= 0; pos--) {
            for (int switched = 1; switched >= 0; switched --) {
                for (int lane = 0; lane < 3; lane++) {
                    // forward jump
                    if (obstacles[pos + 1] != lane + 1)
                        solutions[pos][switched][lane] = solutions[pos + 1][0][lane];

                    if (switched == 0) {
                        for (int delta = -1; delta <= 1; delta += 2) {
                            int alt = (lane + delta + 3) % 3;

                            if (obstacles[pos] != alt + 1) {
                                solutions[pos][switched][lane] = Math.min(
                                    solutions[pos][switched][lane],
                                    1 + solutions[pos][1][alt]
                                );
                            }
                        }
                    }
                }
            }
        }

        return solutions[0][0][1];
    }
}
