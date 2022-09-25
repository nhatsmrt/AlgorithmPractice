def range_sum(begin, end, prefixes):
    # sum(piles[begin:end])
    return prefixes[end] - prefixes[begin]

def max_score(piles, begin, end, solutions, prefixes):
    # subproblem: max stonnes current player can get
    # if he has to pick the ends of piles[begin:end]
    # i.e piles[begin] or piles[end - 1]

    # base case: 0 number left
    if begin == end:
        return 0

    if (begin, end) in solutions:
        return solutions[(begin, end)]

    ret = max(
        # choose piles[begin], and let opponent play on piles[begin + 1:end]
        piles[begin] + range_sum(begin + 1, end, prefixes) - max_score(piles, begin + 1, end, solutions, prefixes),
        # choose piles[end - 1], and let opponent play on piles[begin:end - 1]
        piles[end - 1] + range_sum(begin, end - 1, prefixes) - max_score(piles, begin, end - 1, solutions, prefixes),
    )

    solutions[(begin, end)] = ret
    return ret


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Time and Space Complexity: O(N^2)

        prefixes = [0] + list(accumulate(piles))
        return max_score(piles, 0, len(piles), {}, prefixes) >= prefixes[-1] / 2
        
