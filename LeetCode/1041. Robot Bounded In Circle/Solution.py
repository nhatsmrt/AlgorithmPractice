class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # Observation 1: after 1 cycle, if robot ends up in (0, 0),
        # then the trajectory is bounded

        # Observation 2: after 1 cycle, if the robot does not face upward,
        # then after 4 cycles, the robot will end up in (0, 0),
        # so the trajectory is also bounded.

        # Time Complexity: O(N)
        # Space Complexity: O(1)

        x, y, direction = 0, 0, 0
        steps = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

        for ins in instructions:
            if ins == "G":
                x, y = x + steps[direction][0], y + steps[direction][1]
            elif ins == "L":
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4

        return (x, y) == (0, 0) or direction != 0
