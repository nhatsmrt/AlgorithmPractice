from collections import deque, Counter


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cnt = Counter()
        self.data = deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.data) > 0 and self.cnt[self.data[0]] > 1:
            self.data.popleft()

        if len(self.data) > 0:
            return self.data[0]
        return -1

    def add(self, value: int) -> None:
        self.cnt[value] += 1
        self.data.append(value)



# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
