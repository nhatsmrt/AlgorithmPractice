class SparseVector:
    def __init__(self, nums: List[int]):
        # Time Complexity: O(N)
        # Space Complexity: O(L)

        self.data = defaultdict(lambda: 0)

        for i, num in enumerate(nums):
            if num:
                self.data[i] = num


    def __getitem__(self, i: int) -> int:
        return self.data[i]


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # Time Complexity: O(min(L1, L2))

        if len(self) > len(vec):
            return vec.dotProduct(self)

        ret = 0
        for i in self.data:
            ret += self.data[i] * vec[i]

        return ret


    def __len__(self) -> int:
        return len(self.data)


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
