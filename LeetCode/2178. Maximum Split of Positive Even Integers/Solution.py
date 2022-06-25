class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # Time and Space Complexity: O(Q)
        # Where Q is the size of the answer set

        # we have: 1 + 2 + ... + Q < N
        # Q(Q + 1) / 2 < N
        # So Q = O(sqrt(N))

        # Greedy proof: use exchange argument

        if finalSum % 2 == 1: # odd
            return []

        target = finalSum // 2
        ret = []

        lower_bound = 1
        ret = []
        while target > 0:
            if lower_bound * 2 + 1 > target:
                choice = target
            else:
                choice = lower_bound

            lower_bound += 1
            target -= choice

            ret.append(choice * 2)

        return ret
