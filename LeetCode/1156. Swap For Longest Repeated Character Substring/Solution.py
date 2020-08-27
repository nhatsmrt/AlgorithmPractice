class Interval:
    def __init__(self, start, end):
        self.start, self.end = start, end

    def __len__(self):
        return self.end - self.start + 1

    def __repr__(self):
        return repr([self.start, self.end])


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # Time and Space Complexity: O(N)

        index = {}

        for i in range(len(text)):
            if text[i] not in index:
                index[text[i]] = []

            index[text[i]].append(i)

        ret = 0
        for char in index:
            ret = max(ret, self.find_longest(index[char]))

        return ret

    def find_longest(self, occ: List[int]) -> int:
        intervals = []

        start = 0
        while start < len(occ):
            end = start

            while end + 1 < len(occ) and occ[end + 1] == occ[end] + 1:
                end += 1

            intervals.append(Interval(occ[start], occ[end]))
            start = end + 1

        if len(intervals) == 1:
            return len(intervals[0])
        else:
            ret = max(map(len, intervals)) + 1

            for i in range(len(intervals) - 1):
                if intervals[i].end + 2 == intervals[i + 1].start:
                    candidate = len(intervals[i]) + len(intervals[i + 1])

                    if candidate < len(occ):
                        candidate += 1

                    ret = max(ret,  candidate)

            return ret
