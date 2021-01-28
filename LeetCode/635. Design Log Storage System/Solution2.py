from sortedcontainers import SortedDict


class LogSystem:

    def __init__(self):
        self.tweets = SortedDict()
        self.granularity = {
            "Year": 0,
            "Month": 1,
            "Day": 2,
            "Hour": 3,
            "Minute": 4,
            "Second": 5,
        }

        self.min = ["2000", "01", "01", "00", "00", "00"]
        self.max = ["2017", "12", "31", "23", "59", "59"]


    def put(self, id: int, timestamp: str) -> None:
        # Time Complexity: O(log N)
        self.tweets[timestamp] = id


    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        # Time Complexity: O(num_answer + log N)

        ret = []
        gran_s = self.granularize(s, gra, True)
        gran_e = self.granularize(e, gra, False)


        for timestamp in self.tweets.irange(gran_s, gran_e):
            ret.append(self.tweets[timestamp])

        return ret


    def granularize(self, timestamp: str, gra: str, start: bool) -> int:
        last_kept = self.granularity[gra]
        components = timestamp.split(":")[:last_kept + 1]

        if start:
            components += self.min[last_kept + 1:]
        else:
            components += self.max[last_kept + 1:]

        return ":".join(components)



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
