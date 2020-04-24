class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for trip in trips:
            events.append((trip[1], 0, trip[0]))
            events.append((trip[2], 1, trip[0]))

        events.sort(key=lambda ev:-ev[1])
        events.sort(key=lambda ev:ev[0])

        time = 0
        cur_passenger = 0

        for event in events:
            time = event[0]

            if event[1] == 0:
                cur_passenger += event[2]
                if cur_passenger > capacity:
                    return False
            else:
                cur_passenger -= event[2]


        return True
                
