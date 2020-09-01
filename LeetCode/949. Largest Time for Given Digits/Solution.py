class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # Time and Space Complexity: O(1)

        indices = itertools.permutations(range(4))
        candidates = map(lambda perm: [A[perm[0]], A[perm[1]], A[perm[2]], A[perm[3]]], indices)
        valid_candidates = list(filter(self.is_valid, candidates))

        if not valid_candidates:
            return ""

        return self.to_str_repr(max(valid_candidates, key=self.to_num_min))

    def is_valid(self, time: List[int]) -> bool:
        hour = time[0] * 10 + time[1]
        minute = time[2] * 10 + time[3]

        return 0 <= hour <= 23 and 0 <= minute <= 59

    def to_num_min(self, time: List[int]) -> int:
        hour = time[0] * 10 + time[1]
        minute = time[2] * 10 + time[3]

        return hour * 60 + minute

    def to_str_repr(self, time: List[int]) -> str:
        hour = str(time[0] * 10 + time[1])
        minute = str(time[2] * 10 + time[3])

        if len(hour) < 2:
            hour = "0" + hour

        if len(minute) < 2:
            minute = "0" + minute

        return hour + ":" + minute
