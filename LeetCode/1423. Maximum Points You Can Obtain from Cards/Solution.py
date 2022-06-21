class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Time and Space Complexity: O(k)

        prefix = [0]
        suffix = [0]

        for i in range(k):
            prefix.append(prefix[-1] + cardPoints[i])
            suffix.append(suffix[-1] + cardPoints[len(cardPoints) - 1 - i])

        ret = 0
        for i in range(k + 1):
            ret = max(ret, prefix[i] + suffix[len(suffix) - 1 - i])

        return ret
