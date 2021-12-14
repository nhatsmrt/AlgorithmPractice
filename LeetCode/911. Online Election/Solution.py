class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # Time and Space Complexity: O(N)

        self.best = []
        cnter = Counter()
        winner = None

        for person, time in zip(persons, times):
            cnter[person] += 1

            if winner is None or cnter[winner] <= cnter[person]:
                winner = person
                self.best.append((winner, time))

    def q(self, t: int) -> int:
        # Time Complexity: O(log N)
        # Space Complexity: O(1)

        low, high = 0, len(self.best) - 1

        while low < high:
            mid = high - (high - low) // 2
            winner, time = self.best[mid]

            if time > t:
                high = mid - 1
            else:
                low = mid

        return self.best[low][0]





# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
