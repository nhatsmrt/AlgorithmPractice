from functools import partial
from itertools import starmap


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Time and Space Complexity: O(N^2) (potentially O(N sqrt N))
        self.index = {}
        for i in range(len(stones)):
            self.index[stones[i]] = i

        self.dp = {}
        if stones[1] != 1:
            return False

        return self.canCrossDP(stones, 1, 1)

    def canCrossDP(self, stones, i: int, prev: int) -> bool:
        if (i, prev) in self.dp:
            return self.dp[(i, prev)]

        if i == len(stones) - 1:
            ret = True
        else:
            next_jump_length = [prev - 1, prev, prev + 1]
            next_spots = map(lambda step: step + stones[i], next_jump_length)
            next_landing_index = map(lambda spot: self.index.get(spot, -1), next_spots)

            next_state = filter(lambda state: state[0] > -1 and state[1] > 0, zip(next_landing_index, next_jump_length))
            ret = any(starmap(partial(self.canCrossDP, stones), next_state))

        self.dp[(i, prev)] = ret
        return ret
