class Solution:

    def __init__(self, nums: List[int]):
        # Time and Space Complexity: O(N)
        self.index = {}

        for i, val in enumerate(nums):
            if val not in self.index:
                self.index[val] = []

            self.index[val].append(i)


    def pick(self, target: int) -> int:
        # Time and Space Complexity: O(1)
        occs = self.index[target]
        return occs[random.randrange(len(occs))]



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
