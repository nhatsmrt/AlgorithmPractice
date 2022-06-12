class Solution:
    def racecar(self, target: int) -> int:
        # Time and Space Complexity: O(target log(target))

        init = (target, 1)

        traverse = deque()
        traverse.append((0, init))

        visited = set()
        visited.add(init)

        while traverse:
            step, (dist, speed) = traverse.popleft()

            if not dist:
                return step

            new_step = step + 1
            # R:
            if speed > 0:
                new_speed = -1
            else:
                new_speed = 1

            if (dist, new_speed) not in visited:
                visited.add((dist, new_speed))
                traverse.append((new_step, (dist, new_speed)))


            # A:
            new_dist = dist - speed
            new_speed = speed * 2

            if new_dist < 0:
                new_dist = -new_dist
                new_speed = -new_speed

            if (new_dist, new_speed) not in visited and new_dist <= target:
                visited.add((new_dist, new_speed))
                traverse.append((new_step, (new_dist, new_speed)))
