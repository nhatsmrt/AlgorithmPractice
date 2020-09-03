class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # Time and Space Complexity: O(N)

        cur = 0

        ret = []
        for num in target:
            for _ in range(cur, num - 1):
                ret.extend(["Push", "Pop"])

            ret.append("Push")
            cur = num

        return ret
