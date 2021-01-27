import sortedcontainers


class TweetCounts:

    def __init__(self):
        self.tweets = {}
        self.freqToDuration = {
            "minute": 60,
            "hour": 60 * 60,
            "day": 60 * 60 * 24
        }



    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.tweets:
            self.tweets[tweetName] = []

        self.tweets[tweetName].append(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        duration = self.freqToDuration[freq]
        num_interval = math.ceil((endTime - startTime + 1) / duration)
        ret = [0] * num_interval

        for time in self.tweets.get(tweetName, []):
            if time >= startTime and time <= endTime:
                interval = (time - startTime) // duration
                ret[interval] += 1

        return ret

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
