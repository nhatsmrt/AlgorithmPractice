class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        # Time and Space Complexity: O(N^2)

        ready = []
        window_to_not_ready = {i: set() for i in range(len(target) - len(stamp) + 1)}
        not_ready_to_window = {i: set() for i in range(len(target))}

        for i in range(len(target) - len(stamp) + 1):
            for j in range(len(stamp)):
                if target[i + j] != stamp[j]:
                    not_ready_to_window[i + j].add(i)
                    window_to_not_ready[i].add(i + j)

            if not window_to_not_ready[i]:
                ready.append(i)


        covered = set()
        ret = []

        while ready and len(covered) < len(target):
            stamp_ind = ready.pop()
            ret.append(stamp_ind)

            for j in range(len(stamp)):
                covered.add(stamp_ind + j)

                for window_ind in not_ready_to_window[stamp_ind + j]:
                    window_to_not_ready[window_ind].remove(stamp_ind + j)

                    if not window_to_not_ready[window_ind]:
                        ready.append(window_ind)

                not_ready_to_window[stamp_ind + j] = set()


        if len(covered) == len(target):
            return list(reversed(ret))

        return []
