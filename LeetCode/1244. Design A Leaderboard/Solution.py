class Leaderboard:

    def __init__(self):
        self.data = {}

    def addScore(self, playerId: int, score: int) -> None:
        # Time Complexity: O(1) per query
        self.data[playerId] = self.data.get(playerId, 0) + score

    def top(self, K: int) -> int:
        # Time Complexity: O(L log L), where L is number of players
        return sum(sorted(self.data.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        # Time Complexity: O(1) per query
        self.data.pop(playerId)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
