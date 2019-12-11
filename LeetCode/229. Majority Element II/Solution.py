class CountMinSketch:
    def __init__(self):
        self.frequencies = [
            [0 for _ in range(19)],
            [0 for _ in range(7)]
        ]
        self.hashes = [
            lambda x: (x * 3) % 19,
            lambda x: (x * 5) % 7
        ]
        # self.n_elements = 0  # Turn on if want to keep track of num elements

    def increment(self, value):
        for i in range(len(self.frequencies)):
            self.frequencies[i][self.hashes[i](value)] += 1
        # self.n_elements += 1  # Turn on if want to keep track of num elements

    def estimate(self, value):
        return min(
            [
                self.frequencies[i][self.hashes[i](value)]
                for i in range(len(self.frequencies))
            ]
        )

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ret = []
        all_values = set()
        maj_criterion = len(nums) // 3
        estimator = CountMinSketch()

        for value in nums:
            estimator.increment(value)
            all_values.add(value)

        for value in all_values:
            if estimator.estimate(value) > maj_criterion:
                ret.append(value)

        return ret
        
