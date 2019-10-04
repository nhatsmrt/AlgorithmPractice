class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        int x = 0;
        int y = 0;
        int dir = 0; //0 : up, 1: right, 2: down, 3: left
        int ret = 0;

        Map<Integer, Set<Integer>> obstaclesMap = new HashMap<Integer, Set<Integer>>();

        for (int[] obstacle : obstacles) {
            if (!obstaclesMap.containsKey(obstacle[0]))
                obstaclesMap.put(obstacle[0], new HashSet<Integer>());
            obstaclesMap.get(obstacle[0]).add(obstacle[1]);
        }

        for (int command : commands) {
            if (command >= 1 && command <= 9) {
                int newX = x;
                int newY = y;

                for (int s = 0; s < command; s++) {
                    if (dir == 0)
                        newY += 1;
                    else if (dir == 1)
                        newX += 1;
                    else if (dir == 2)
                        newY -= 1;
                    else if (dir == 3)
                        newX -= 1;

                    if (obstaclesMap.containsKey(newX) && obstaclesMap.get(newX).contains(newY))
                        break;
                    else {
                        x = newX;
                        y = newY;
                        ret = Math.max(ret, x * x + y * y);
                    }
                }
            }
            else {
                if (command == -1)
                    dir += 1;
                else if (command == -2)
                    dir += 3;

                dir %= 4;
            }
        }

        return ret;
    }
}
