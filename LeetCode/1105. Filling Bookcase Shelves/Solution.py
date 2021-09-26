from sortedcontainers import SortedList


class IntervalSet:
    def __init__(self, dp):
        # intervals: (start, end, height, value)
        # values: sorted list

        self.dp = dp
        self.intervals = deque()
        self.values = SortedList()

    def add(self, new_height, new_start, max_end):
        # pop out of reach values
        while self.intervals and self.intervals[0][1] > max_end:
            start, end, height, value = self.intervals.popleft()
            self.values.remove(value)

            if start <= max_end:
                self.intervals.appendleft((start, max_end, height, self.dp[max_end + 1] + height))
                self.values.add(self.dp[max_end + 1] + height)

        new_end, new_value = new_start, self.dp[new_start + 1] + new_height

        while self.intervals and new_height >= self.intervals[-1][2]:
            _, new_end, height, value = self.intervals.pop()

            self.values.remove(value)
            new_value = new_height + self.dp[new_end + 1]

        self.intervals.append((new_start, new_end, new_height, new_value))
        self.values.add(new_value)

    def get_min(self):
        return self.values[0]



class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        # dp[i] = min height to place books from books[i]
        # dp[len(books)] = 0
        # dp[i] = min_{i <= j <= len(books) - 1} max(books[i: j + 1]) + dp[j + 1]
        # as long as width <= shelfWidth


        # Observation 1: if x < y, then dp[x] >= dp[y]
        # Observation 2: we can maintain the intervals in which hmax doesn't change
        # Observation 3: if hmax doesn't change over [x1, x2], and x1 < y < x2
        # then max(books[i:y]) = max(books[i:x2]) and dp[y] >= dp[x2]
        # so we don't need to consider x2

        dp = [100000000] * (len(books) + 1)
        dp[-1] = 0

        max_ends = []
        start = 0
        end = 0
        width = books[0][0]

        while start < len(books):
            if end + 1 < len(books) and width + books[end + 1][0] <= shelfWidth:
                end += 1
                width += books[end][0]
            else:
                max_ends.append(end)

                if start < end:
                    width -= books[start][0]
                    start += 1
                else:
                    end += 1
                    start = end
                    width = 0

                    if start < len(books):
                        width += books[start][0]

        intervals = IntervalSet(dp)

        for i in range(len(books) - 1, -1, -1):
            intervals.add(books[i][1], i, max_ends[i])
            dp[i] = intervals.get_min()

        return dp[0]
