class RangeFreqQuery:
    # Time Complexity: <O(N log N), O(log N)>
    # Space Complexity: O(N log N)

    def __init__(self, arr: List[int]):
        self.node = {} # range -> counter
        self.max_ind = len(arr) - 1
        self._build(arr, 0, len(arr) - 1)

    def _build(self, arr, start, end):
        if start == end:
            self.node[(start, start)] = Counter(arr[start:end + 1])
        else:
            mid = start + (end - start) // 2
            self._build(arr, start, mid)
            self._build(arr, mid + 1, end)

            self.node[(start, end)] = self.node[(start, mid)] + self.node[(mid + 1, end)]

    def query(self, left: int, right: int, value: int) -> int:
        return self._query(left, right, value, 0, self.max_ind)

    def _query(self, left, right, value, start, end):
        if right < start or left > end:
            return 0

        if left <= start and end <= right:
            return self.node[(start, end)][value]

        mid = start + (end - start) // 2
        return self._query(left, right, value, start, mid) + self._query(left, right, value, mid + 1, end)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
