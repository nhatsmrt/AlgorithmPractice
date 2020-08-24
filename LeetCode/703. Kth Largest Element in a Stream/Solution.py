class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Time Complexity: O(K log (N) + N)
        # Space Complexity: O(K)

        self.k = k

        nums = list(map(lambda val: -val, nums))
        heapq.heapify(nums)

        self.data = []
        to_add = min(k, len(nums))

        for i in range(to_add):
            self.data.append(-heapq.heappop(nums))

    def add(self, val: int) -> int:
        # Time Complexity: O(K)

        pos = self.find(val)

        if len(self.data) < self.k:
            self.data.append(-1)

        if pos < self.k:
            self.put(val, pos)

        return self.data[-1]

    def put(self, val: int, pos: int):
        for i in range(len(self.data) - 1, pos, -1):
            self.data[i] = self.data[i - 1]

        self.data[pos] = val

    def find(self, val: int) -> int:
        low = 0
        high = len(self.data)

        while low < high:
            mid = low + (high - low) // 2

            if self.data[mid] < val:
                high = mid
            else:
                low = mid + 1

        return low


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
