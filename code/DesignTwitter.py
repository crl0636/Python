import collections
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_dict = collections.defaultdict(list)
        self.follow_dict = collections.defaultdict(set)
        self.count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.count += 1
        self.user_dict[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news
        feed must be posted by users who the user followed or by the user herself.
        Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = []
        tweets += self.user_dict[userId]

        for other in self.follow_dict[userId]:
            tweets += self.user_dict[other]

        last_ten = sorted(tweets)[-10:]
        print last_ten
        return [tweetId for _, tweetId in last_ten[::-1]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.follow_dict[followerId].discard(followeeId)
