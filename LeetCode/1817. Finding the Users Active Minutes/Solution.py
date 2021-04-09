class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Time and Space Complexity: O(N)

        minutes = {}

        for user, minute in logs:
            if user not in minutes:
                minutes[user] = set()

            minutes[user].add(minute)

        ret = [0] * k
        for user in minutes:
            ret[len(minutes[user]) - 1] += 1

        return ret
