from sortedcontainers import SortedSet

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # Time Complexity: O((n + k) log k)
        # Space Complexity: O(n)

        nodes = SortedSet(range(k))
        machine_used = []
        used_cnt = Counter()

        for req_ind, (arr_time, dur) in enumerate(zip(arrival, load)):
            while machine_used and machine_used[0][0] <= arr_time:
                _, machine_ind = heapq.heappop(machine_used)
                nodes.add(machine_ind)

            if nodes:
                machine_ind = nodes[(nodes.bisect_left(req_ind % k)) % len(nodes)]
                nodes.remove(machine_ind)
                used_cnt[machine_ind] += 1
                heapq.heappush(machine_used, (arr_time + dur, machine_ind))

        ret = []
        max_use = -1

        for machine_ind in range(k):
            if used_cnt[machine_ind] == max_use:
                ret.append(machine_ind)
            elif used_cnt[machine_ind] > max_use:
                max_use = used_cnt[machine_ind]
                ret = [machine_ind]

        return ret
