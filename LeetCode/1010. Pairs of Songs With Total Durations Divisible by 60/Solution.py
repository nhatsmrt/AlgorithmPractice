class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = Counter()

        for t in time:
            counter[t % 60] += 1


        ret = 0
        for t in counter:
            if t == 30 or t == 0:
                ret += counter[t] * (counter[t] - 1) // 2
            elif t < 60 - t:
                ret += counter[t] * counter[60 - t]

        return ret
