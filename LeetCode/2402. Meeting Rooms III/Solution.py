MEETING_START = 1
MEETING_END = 0


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Time Complexity: O(M log MN)
        # Space Complexity: O(N + M)

        events = [(start, MEETING_START, end - start) for start, end in meetings]
        pending = []
        available_rooms = list(range(n))
        heapq.heapify(events)

        meeting_cnter = Counter()

        while events:
            event = heapq.heappop(events)
            event_type = event[1]
            cur_time = event[0]

            if event_type == MEETING_START:
                duration = event[2]

                if available_rooms:
                    room = heapq.heappop(available_rooms)
                    heapq.heappush(events, (cur_time + duration, MEETING_END, room))
                    meeting_cnter[room] += 1
                else:
                    heapq.heappush(pending, (cur_time, duration))
            elif event_type == MEETING_END:
                room = event[2]

                if pending:
                    _, duration = heapq.heappop(pending)
                    heapq.heappush(events, (cur_time + duration, MEETING_END, room))
                    meeting_cnter[room] += 1
                else:
                    heapq.heappush(available_rooms, room)

        ret = 0
        for room in range(n):
            if meeting_cnter[room] > meeting_cnter[ret]:
                ret = room

        return ret
