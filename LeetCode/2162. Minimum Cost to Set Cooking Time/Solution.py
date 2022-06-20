class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # Time and Space Complexity: O(1)

        def compute_cost(digits: List[int]) -> int:
            cur = startAt
            ret = 0

            for dig in digits:
                if dig != cur:
                    ret += moveCost

                ret += pushCost
                cur = dig

            return ret

        def build_cand(minute, second):
            ret = []

            if minute:
                ret.extend(map(int, str(minute)))

            if minute and second < 10:
                ret.append(0)

            ret.extend(map(int, str(second)))

            return ret


        def get_candidate(targetSeconds: int) -> List[List[int]]:
            # "canonical" representation:
            second = targetSeconds % 60
            minute = targetSeconds // 60

            ret = [build_cand(minute, second)]

            if minute > 0 and second <= 39:
                minute -= 1
                second += 60

                ret.append(build_cand(minute, second))

            return ret

        return min(map(compute_cost, filter(lambda cand: len(cand) <= 4, get_candidate(targetSeconds))))
