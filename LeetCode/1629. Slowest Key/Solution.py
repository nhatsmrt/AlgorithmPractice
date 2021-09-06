class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # Time and Space Complexity: O(N)
        durations = {}
        for i, char in enumerate(keysPressed):
            start = 0 if not i else releaseTimes[i - 1]
            duration = releaseTimes[i] - start
            durations[char] = max(duration, durations.get(char, 0))

        return max([(durations[char], char) for char in durations])[1]
