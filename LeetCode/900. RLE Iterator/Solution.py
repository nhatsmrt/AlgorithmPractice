class RLEIterator:

    def __init__(self, A: List[int]):
        # TIme and Space Complexity: O(N)
        data = []
        cum = 0

        for i in range(0, len(A), 2):
            if A[i]:
                cum += A[i]
                data.append((cum, A[i + 1]))

        self.data = data
        self.used = 0
        self.ind = 0


    def next(self, n: int) -> int:
        # Time Complexity: O(log N) (N is length of RLE array)
        # Space Complexity: O(1)
        low = self.ind
        high = len(self.data) - 1

        while low < high:
            mid = low + (high - low) // 2

            if self.data[mid][0] - self.used < n:
                low = mid + 1
            else:
                high = mid

        if self.data[low][0] - self.used >= n:
            self.data_ind = low
            self.used += n

            return self.data[low][1]
        else:
            self.data_ind = len(self.data)
            self.used = self.data[-1][0]
            return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
