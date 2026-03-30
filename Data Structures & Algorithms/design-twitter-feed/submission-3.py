class Twitter:

    def __init__(self):
        self.tweets = {}
        self.followMap = {}
        self.timeStamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((tweetId, self.timeStamp))
        self.timeStamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        heap = []
        res = []
        for followee in self.followMap[userId]:
            if followee in self.tweets:
                tweetId, time = self.tweets[followee][-1]
                heapq.heappush(heap, (time, tweetId, len(self.tweets[followee])-1, followee))
        while len(res) < 10 and heap:
            curTime, curTweetId, Idx, curFollowee = heapq.heappop(heap)
            res.append(curTweetId)
            if Idx > 0:
                if curFollowee in self.tweets:
                    tweetId, time = self.tweets[curFollowee][Idx-1]
                    heapq.heappush(heap, (time, tweetId, Idx-1, curFollowee))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap:
            self.followMap[followerId] = set()
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
