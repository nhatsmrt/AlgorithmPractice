class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        tasks = sorted(enumerate(tasks), key=lambda task: task[1][0]) # sort by enqueue time
        ret = []

        cur_time = 0
        ready = []
        i = 0

        while ready or i < len(tasks):
            while i < len(tasks) and tasks[i][1][0] <= cur_time:
                heapq.heappush(ready, (tasks[i][1][1], tasks[i][0]))
                i += 1

            if ready:
                next_time, next_id = heapq.heappop(ready)
                cur_time += next_time
                ret.append(next_id)
            else:
                cur_time = tasks[i][1][0]

        return ret
