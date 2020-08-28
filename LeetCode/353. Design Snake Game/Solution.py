class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.positions = collections.deque()
        self.positions_set = set()
        self.positions.append((0, 0))
        self.positions_set.add((0, 0))

        self.width, self.height, self.food = width, height, list(map(tuple, food))
        self.moves = {
            "R": (0, 1),
            "D": (1, 0),
            "U": (-1, 0),
            "L": (0, -1)
        }

        self.eaten = 0



    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        # O(1) per move

        cur_pos = self.positions[-1]

        move = self.moves[direction]
        new_pos = cur_pos[0] + move[0], cur_pos[1] + move[1]

        if new_pos[0] == self.height or new_pos[0] == -1 or new_pos[1] == self.width or new_pos[1] == -1 or (new_pos in self.positions_set and new_pos != self.positions[0]):
            return -1

        self.positions.append(new_pos)
        self.positions_set.add(new_pos)

        if self.eaten < len(self.food) and new_pos == self.food[self.eaten]:
            self.eaten += 1
        else:
            tail = self.positions.popleft()

            if tail != self.positions[-1]:
                self.positions_set.remove(tail)

        return self.eaten


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
