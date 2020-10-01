class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.followees = {}
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # Time Complexity: O(1)
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((-self.timestamp, tweetId))
        self.timestamp += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        # Time Complexity: O(num_user)
        data = []
        ret = []

        if userId in self.tweets:
            data.append((self.tweets[userId][-1], userId, len(self.tweets[userId]) - 1))

        for follow in self.followees.get(userId, []):
            if follow in self.tweets:
                data.append((self.tweets[follow][-1], follow, len(self.tweets[follow]) - 1))

        heapq.heapify(data)

        for _ in range(10):
            if not data:
                break

            (_, tweet_id), user_id, user_ind = heapq.heappop(data)
            ret.append(tweet_id)

            if user_ind > 0:
                heapq.heappush(data, (self.tweets[user_id][user_ind - 1], user_id, user_ind - 1))

        return ret


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        # Time Complexity: O(1)
        if followerId != followeeId:
            if followerId not in self.followees:
                self.followees[followerId] = set()

            self.followees[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        # Time Complexity: O(1)
        if followerId in self.followees and followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
