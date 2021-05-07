class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Time Complexity: O(N (log W + log N))
        # Space Complexity: O(N)

        penalty_low = 0
        penalty_high = max([event[-1] for event in events]) + 1
        events.sort(key=lambda ev: (ev[0], ev[1]))

        self.next = []
        for i, event in enumerate(events):
            low = i + 1
            high = len(events)

            while low < high:
                mid = (low + high) // 2

                if events[mid][0] <= events[i][1]:
                    low = mid + 1
                else:
                    high = mid

            self.next.append(low)

        ret = 0


        while penalty_low < penalty_high:
            penalty = (penalty_low + penalty_high) // 2

            self.dp = {}
            max_sum1, num_choose1 = self.max_sum(events, 0, penalty, True)

            self.dp = {}
            max_sum2, num_choose2 = self.max_sum(events, 0, penalty, False)

            if k < num_choose1: # penalty is too low:
                penalty_low = penalty + 1
            else:
                num_choose = min(k, num_choose2)
                ret = max(ret, max_sum1 + penalty * num_choose)
                penalty_high = penalty - 1

        return ret


    def max_sum(self, events: List[List[int]], i: int, penalty: int, min_choose: bool):
        if i == len(events):
            return 0, 0

        if i in self.dp:
            return self.dp[i]

        max_sum1 = events[i][-1] - penalty
        max_sum_next, num_choose_next = self.max_sum(events, self.next[i], penalty, min_choose)
        num_choose1 = 1 + num_choose_next
        max_sum1 += max_sum_next


        max_sum2, num_choose2 = self.max_sum(events, i + 1, penalty, min_choose)

        if max_sum1 > max_sum2:
            ret = max_sum1, num_choose1
        elif max_sum2 > max_sum1:
            ret = max_sum2, num_choose2
        elif min_choose:  # choose as few as possible
            if num_choose1 < num_choose2:
                ret = max_sum1, num_choose1
            else:
                ret = max_sum2, num_choose2
        else: # choose as many as possible
            if num_choose2 < num_choose1:
                ret = max_sum1, num_choose1
            else:
                ret = max_sum2, num_choose2

        self.dp[i] = ret
        return ret
