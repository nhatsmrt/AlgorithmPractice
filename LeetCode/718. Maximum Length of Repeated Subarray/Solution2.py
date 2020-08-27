class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # Time and Space Complexity (on average): O((M + N) log(min(M, N)))

        low, high = 0, min(len(A), len(B))

        while low < high:
            mid = high - (high - low) // 2

            if self.check(A, B, mid):
                low = mid
            else:
                high = mid - 1

        return low

    def check(self, A: List[int], B: List[int], length: int) -> bool:
        if not length:
            return True

        index_A = self.compute_rolling_hash_index(A, length)
        index_B = self.compute_rolling_hash_index(B, length)

        for key in index_A.keys() & index_B.keys():
            for start_A in index_A[key]:
                for start_B in index_B[key]:
                    if A[start_A:start_A + length] == B[start_B:start_B + length]:
                        return True

        return False

    def compute_rolling_hash_index(self, A: List[int], length: int) -> dict:
        hash_A = RollingHash()
        for i in range(length):
            hash_A.add(A[i])

        index = {hash_A.hash: [0]}
        for i in range(length, len(A)):
            hash_A.remove(A[i - length])
            hash_A.add(A[i])

            cur_hash = hash_A.hash

            if cur_hash not in index:
                index[cur_hash] = []

            index[cur_hash].append(i - length + 1)

        return index

class RollingHash:
    def __init__(self):
        self.hash = 0
        self.mod = 37
        self.pow = 100
        self.length = 0

    def add(self, val: int):
        self.hash = (self.hash * self.pow + val) % self.mod
        self.length += 1

    def remove(self, val: int):
        self.hash = (self.hash - val * (self.pow ** (self.length - 1))) % self.mod
        self.length -= 1
