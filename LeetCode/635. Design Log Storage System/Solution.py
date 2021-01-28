class LogSystem:

    def __init__(self):
        self.tweets = {}
        self.granularity = {
            "Year": 0,
            "Month": 1,
            "Day": 2,
            "Hour": 3,
            "Minute": 4,
            "Second": 5,
        }


    def put(self, id: int, timestamp: str) -> None:
        self.tweets[id] = timestamp


    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        ret = []
        gran_s = self.granularize(s, gra)
        gran_e = self.granularize(e, gra)

        for tweet in self.tweets:
            gran_ts = self.granularize(self.tweets[tweet], gra)

            if gran_s <= gran_ts and gran_ts <= gran_e:
                ret.append(tweet)

        return ret


    def granularize(self, timestamp: str, gra: str) -> int:
        components = timestamp.split(":")
        return ":".join(components[:self.granularity[gra] + 1])



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
