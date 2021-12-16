class Solution:
    def sortSentence(self, s: str) -> str:
        # Time and Space Complexity: O(N)

        words = sorted(s.split(" "), key=itemgetter(-1))
        return " ".join(map(lambda w: w[:-1], words))
