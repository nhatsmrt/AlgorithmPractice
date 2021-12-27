from sortedcontainers import SortedList


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)
        lefts = []
        rights = []
        stores = [lefts, rights]

        for i, rating in enumerate([rating, reversed(rating)]):
            sorted_rating = SortedList()
            for r in rating:
                smaller = sorted_rating.bisect_left(r)
                larger = len(sorted_rating) - smaller

                stores[i].append((smaller, larger))
                sorted_rating.add(r)

        rights = rights[::-1]
        ret = 0
        for (smaller_left, larger_left), (smaller_right, larger_right) in zip(lefts, rights):
            ret += smaller_left * larger_right + larger_left * smaller_right

        return ret
