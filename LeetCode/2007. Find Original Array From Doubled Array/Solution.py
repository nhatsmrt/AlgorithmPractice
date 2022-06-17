class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        changed.sort()

        cnter = Counter(changed)

        ret = []

        for val in changed:
            if cnter[val] > 0:
                cnter[val] -= 1

                if cnter[val * 2] == 0:
                    return []

                cnter[val * 2] -= 1
                ret.append(val)

        return ret
