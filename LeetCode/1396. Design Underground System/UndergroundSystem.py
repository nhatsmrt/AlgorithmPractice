class UndergroundSystem:

    def __init__(self):
        # Time Complexity: O(1) per query
        # Space Complexity: O(checkIn + station^2)

        self.avg_time = {}
        self.checked_in = {}


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t_in = self.checked_in.pop(id)
        endStation, t_out = stationName, t

        if (startStation, endStation) not in self.avg_time:
            self.avg_time[(startStation, endStation)] = (t_out - t_in, 1)
        else:
            total_time, n_occur = self.avg_time.pop((startStation, endStation))
            self.avg_time[(startStation, endStation)] = (
                (t_out - t_in + total_time * n_occur) / (n_occur + 1),
                n_occur + 1
            )


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg_time[(startStation, endStation)][0]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
