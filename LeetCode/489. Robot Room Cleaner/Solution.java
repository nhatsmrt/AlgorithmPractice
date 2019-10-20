/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * interface Robot {
 *     // Returns true if the cell in front is open and robot moves into the cell.
 *     // Returns false if the cell in front is blocked and robot stays in the current cell.
 *     public boolean move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     public void turnLeft();
 *     public void turnRight();
 *
 *     // Clean the current cell.
 *     public void clean();
 * }
 */
class Solution {
    Set<Coordinate> explored;

    public void cleanRoom(Robot robot) {
        explored = new HashSet<Coordinate>();
        explored.add(new Coordinate(0, 0));
        explore(robot, 0, 0);
    }

    private void explore(Robot robot, int i, int j) {
        robot.clean();

        Coordinate next = new Coordinate(i, j + 1);
        if (!explored.contains(next)) {
            explored.add(next);
            if (robot.move()) {
                explore(robot, i, j + 1);
                moveBackward(robot);
            }
        }

        robot.turnLeft();
        next = new Coordinate(i - 1, j);
        if (!explored.contains(next)) {
            explored.add(next);
            if (robot.move()) {
                robot.turnRight();
                explore(robot, i - 1, j);
                robot.turnRight();
                robot.move();
                robot.turnRight();
                robot.turnRight();

            }
        }
        robot.turnRight();

        robot.turnLeft();
        robot.turnLeft();
        next = new Coordinate(i, j - 1);
        if (!explored.contains(next)) {
            explored.add(next);
            if (robot.move()) {
                robot.turnRight();
                robot.turnRight();
                explore(robot, i, j - 1);
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
        }
        robot.turnRight();
        robot.turnRight();

        robot.turnRight();
        next = new Coordinate(i + 1, j);
        if (!explored.contains(next)) {
            explored.add(next);
            if (robot.move()) {
                robot.turnLeft();
                explore(robot, i + 1, j);
                robot.turnLeft();
                robot.move();
                robot.turnRight();
                robot.turnRight();
            }
        }
        robot.turnLeft();

    }

    private void moveBackward(Robot robot) {
        robot.turnLeft();
        robot.turnLeft();
        robot.move();
        robot.turnLeft();
        robot.turnLeft();
    }


    private class Coordinate {
        int x;
        int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(final Object otherObj) {
            Coordinate other = (Coordinate) otherObj;
            return x == other.x && y == other.y;
        }


        public int hashCode() {
            return x * 1000000007 + y;
        }
    }
}
