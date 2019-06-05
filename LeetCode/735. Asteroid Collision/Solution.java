class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> st = new Stack<Integer>();
        List<Integer> retList = new ArrayList<Integer>();

        for (int i = asteroids.length - 1; i >= 0; i--) {
            if (asteroids[i] < 0) {
                st.push(asteroids[i]);
            }
            else {
                if (st.isEmpty()) {
                    retList.add(asteroids[i]);
                }
                else {
                    int left = asteroids[i];
                    boolean explode = false;
                    while (!st.isEmpty() && !explode) {
                        int right = st.pop();
                        if (left < -right) {
                            explode = true;
                            st.push(right);
                        }
                        else if (left == -right) {
                            explode = true;
                        }
                    }

                    if (!explode)
                        retList.add(left);
                }
            }
        }

        int[] ret = new int[retList.size() + st.size()];
        int numNeg = st.size();
        for (int i = 0; i < numNeg; i++) {
            ret[i] = st.pop();
        }
        for (int i = numNeg; i < retList.size() + numNeg; i++) {
            ret[i] = retList.get(retList.size() - 1 - i + numNeg);
        }

        return ret;
    }
}
