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
        # Time Complexity: O(log N)
        if tweetName not in self.tweets:
            self.tweets[tweetName] = sortedcontainers.SortedSet()

        self.tweets[tweetName].add(time)


    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        # Time Complexity: O(|intervals| * log N)

        duration = self.freqToDuration[freq]
        num_interval = math.ceil((endTime - startTime + 1) / duration)
        ret = [0] * num_interval

        for i in range(num_interval):
            start = startTime + duration * i
            end = min(endTime + 1, startTime + duration * (i + 1)) - 1

            if tweetName in self.tweets:
                tweets = self.tweets[tweetName]
                ret[i] = tweets.bisect_right(end) - tweets.bisect_left(start)

        return ret

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
