class Solution:

    def __init__(self, rects: List[List[int]]):
        # Time Complexity: <O(N), O(log N)>
        # Space Complexity: O(N)

        self.rects = rects
        prefix = []

        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            if len(prefix) == 0:
                prefix.append(area)
            else:
                prefix.append(area + prefix[-1])

        self.prefix = prefix

    def pick(self) -> List[int]:
        target = random.random() * self.prefix[-1]

        low = 0
        high = len(self.prefix) - 1
        while low < high:
            mid = low + (high - low) // 2

            if self.prefix[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return (
            random.randint(self.rects[low][0], self.rects[low][2]),
            random.randint(self.rects[low][1], self.rects[low][3])
        )



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
