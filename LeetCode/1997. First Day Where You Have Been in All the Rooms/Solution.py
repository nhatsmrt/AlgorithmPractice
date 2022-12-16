class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # Time and Space Complexity: O(N)
        # Observation 1: to visit i, you must have visited 1, 2,..., i - 1
        # Let f(n) = # number of steps to reach n
        # ans = f(len(nextVisit) - 1), f(0) = 0

        # Observation 2: when you're at i and have been here odd times,
        # you have visited all the previous positions odd number of times

        # Observation 3:
        # n > 0: f(n) = 2 + 2 * f(n - 1) - f(nextVisit[n - 1])

        MOD = 10 ** 9 + 7

        steps_to_reach = [0]
        for i in range(1, len(nextVisit)):
            # reaching i - 1:
            steps = steps_to_reach[i - 1]

            # going back:
            steps += 1
            steps %= MOD

            # going forward again
            steps += (steps_to_reach[i - 1] - steps_to_reach[nextVisit[i - 1]])
            steps %= MOD

            # going one last step
            steps += 1
            steps %= MOD

            steps_to_reach.append(steps)

        return steps_to_reach[-1]
