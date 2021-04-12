class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # Time and Space Complexity: O(N)
        ret = [1]
        used = set([1])

        for i in range(k):
            diff = k - i

            if i % 2 == 0:
                ret.append(ret[-1] + diff)
            else:
                ret.append(ret[-1] - diff)
            used.add(ret[-1])


        for i in range(1, n + 1):
            if i not in used:
                ret.append(i)


        return ret
