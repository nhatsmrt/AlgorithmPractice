class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # Time Complexity: O(N^3 K)
        # Space Complexity: O(N^2 K)

        self.dp = {}
        self.prefix = [0] + list(itertools.accumulate(stones))

        ret = self.merge(stones, 0, len(stones) - 1, 1, K)

        return ret

    def merge(self, stones, start: int, end: int, num_parts: int, K: int):
        if (start, end, num_parts) in self.dp:
            return self.dp[(start, end, num_parts)]

        if end - start + 1 < num_parts:
            return -1

        if end - start + 1 == num_parts:
            return 0

        window_sum = self.prefix[end + 1] - self.prefix[start]

        if num_parts == 1:
            split = self.merge(stones, start, end, K, K)

            if split == -1:
                ret = -1
            else:
                ret = window_sum + split
        else:
            candidates = []

            for i in range(start, end):
                left = self.merge(stones, start, i, 1, K)
                right = self.merge(stones, i + 1, end, num_parts - 1, K)

                if left >= 0 and right >= 0:
                    candidates.append(left + right)

            if candidates:
                ret = min(candidates)
            else:
                ret = -1

        self.dp[(start, end, num_parts)] = ret
        return ret
