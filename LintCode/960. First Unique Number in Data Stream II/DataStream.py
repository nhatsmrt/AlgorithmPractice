from collections import Counter, deque


class DataStream:

    def __init__(self):
        # Time Complexity: O(1) per query, amortized
        # Space Complexity: O(N)

        # do intialization if necessary
        self.counter = Counter()
        self.data = deque()

    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if self.counter[num] <= 1:
            self.counter[num] += 1
            self.data.append(num)

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        while self.counter[self.data[0]] > 1:
            self.data.popleft()

        return self.data[0]
