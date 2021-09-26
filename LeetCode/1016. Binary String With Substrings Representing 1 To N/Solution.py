class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # Time Complexity: O(s log(n))
        # Space Complexity: O(n)
        values = set()
        num_digs = math.ceil(math.log2(n))

        for i in range(len(s)):
            if s[i] == "1":
                cur = 1
                values.add(cur)

                for j in range(i + 1, min(len(s), i + num_digs)):
                    cur = cur * 2 + int(s[j])

                    if cur <= n:
                        values.add(cur)

        return len(values) == n
