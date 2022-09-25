def max_stones(values, begin, solutions, suffixes):
    if begin == len(values):
        return 0

    if solutions[begin] is not None:
        return solutions[begin]

    cands = []
    for chosen in range(1, min(4, 1 + len(values) - begin)):
        cand = sum(values[begin:begin + chosen]) + suffixes[begin + chosen] - max_stones(values, begin + chosen, solutions, suffixes)
        cands.append(cand)

    solutions[begin] = max(cands)
    return solutions[begin]


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Time and Space Complexity: O(N)

        suffixes = ([0] + list(accumulate(stoneValue[::-1])))[::-1]
        alice = max_stones(stoneValue, 0, [None] * len(stoneValue), suffixes)

        if alice > suffixes[0] / 2:
            return "Alice"
        elif alice < suffixes[0] / 2:
            return "Bob"
        else:
            return "Tie"
