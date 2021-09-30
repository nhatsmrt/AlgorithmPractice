from sortedcontainers import SortedList


class Leaderboard:

    def __init__(self):
        # Time Complexity: O(1) (init)
        # Space Complexity: O(N) (overall)

        self.scores = {}
        self.sorted_scores = SortedList()


    def addScore(self, playerId: int, score: int) -> None:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)

        if playerId in self.scores:
            self.sorted_scores.remove(self.scores[playerId])
            score += self.scores[playerId]

        self.scores[playerId] = score
        self.sorted_scores.add(score)


    def top(self, K: int) -> int:
        # Time Complexity: O(K) or O(N) (depending on implementation)
        # Space Complexity: O(1)

        start = max(0, len(self.scores) - K)
        return sum(self.sorted_scores.islice(start))

    def reset(self, playerId: int) -> None:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)

        self.addScore(playerId, -self.scores.get(playerId, 0))


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
