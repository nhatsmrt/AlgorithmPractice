def construct(ret, cur_ind, remainders):
    if cur_ind == len(ret): return True

    if ret[cur_ind] is not None:
        return construct(ret, cur_ind + 1, remainders)

    for candidate in sorted(remainders, reverse=True):
        if candidate == 1:
            remainders.remove(1)
            ret[cur_ind] = 1

            if construct(ret, cur_ind + 1, remainders):
                return True

            ret[cur_ind] = None
            remainders.append(1)
        else:
            if cur_ind + candidate >= len(ret):
                return False

            if ret[cur_ind + candidate] is None:
                remainders.remove(candidate)
                ret[cur_ind], ret[cur_ind + candidate] = candidate, candidate

                if construct(ret, cur_ind + 1, remainders):
                    return True

                ret[cur_ind], ret[cur_ind + candidate] = None, None
                remainders.append(candidate)

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Time Complexity: O(n! * (n^2 + (n - 1)^2 + ...)
        # = O(n! * n^3)
        # Space Complexity: O(n^2)

        ret = [None] * (2 * n - 1)
        construct(ret, 0, list(range(1, n + 1)))
        return ret
