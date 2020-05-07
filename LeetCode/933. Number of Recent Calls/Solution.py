from collections import deque


class RecentCounter:

    def __init__(self):
        self.data = deque()


    def ping(self, t: int) -> int:
        while len(self.data) > 0 and self.data[0] < t - 3000:
            self.data.popleft()

        self.data.append(t)
        return len(self.data)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
