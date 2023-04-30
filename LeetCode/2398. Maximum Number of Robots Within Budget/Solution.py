class Window:
    def __init__(self):
        self.sum_vals = 0
        self.values = deque()
        self.len = 0

    def add(self, charge, run):
        self.sum_vals += run

        cnt = 1
        while self.values and self.values[-1][0] <= charge:
            _, old_cnt = self.values.pop()
            cnt += old_cnt

        self.values.append((charge, cnt))
        self.len += 1

    def removefirst(self, run):
        self.sum_vals -= run

        old_value, old_cnt = self.values.popleft()
        if old_cnt > 1:
            self.values.appendleft((old_value, old_cnt - 1))

        self.len -= 1

    def __len__(self):
        return self.len

    def get_window_value(self):
        return self.len * self.sum_vals + self.values[0][0]

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # Time and Space Complexity: O(N)
        start = 0
        window = Window()
        ret = -1

        for end, (charge, run) in enumerate(zip(chargeTimes, runningCosts)):
            window.add(charge, run)

            while window and window.get_window_value() > budget:
                window.removefirst(runningCosts[start])
                start += 1

            if window:
                ret = max(len(window), ret)

        return 0 if ret == -1 else ret
