class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        # Time and Space Complexity: O(N + Q)

        prevs = [[None] * 3]
        prevs[0][colors[0] - 1] = 0
        for i in range(1, len(colors)):
            prevs.append(deepcopy(prevs[-1]))
            prevs[-1][colors[i] - 1] = i

        nexts = [[None] * 3]
        nexts[0][colors[-1] - 1] = len(colors) - 1
        for i in range(len(colors) - 2, -1, -1):
            nexts.append(deepcopy(nexts[-1]))
            nexts[-1][colors[i] - 1] = i

        nexts = nexts[::-1]
        ret = []

        for pos, color in queries:
            next_ind, prev_ind = nexts[pos][color - 1], prevs[pos][color - 1]

            if next_ind is None and prev_ind is None:
                ret.append(-1)
            elif next_ind is None:
                ret.append(pos - prev_ind)
            elif prev_ind is None:
                ret.append(next_ind - pos)
            else:
                ret.append(min(next_ind - pos, pos - prev_ind))

        return ret
