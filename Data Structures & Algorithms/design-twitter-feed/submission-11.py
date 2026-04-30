class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.time = 0
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        heap, res = [], []
        for followee in self.followMap[userId]:
            if followee in self.tweet:
                tweet, time = self.tweet[followee][-1]
                heapq.heappush(heap, (time, tweet, len(self.tweet[followee])-1, followee))
        while len(res) < 10 and heap:
            curT, curTweet, idx, followeeId = heapq.heappop(heap)
            res.append(curTweet)
            if idx > 0:
                Tweet, T = self.tweet[followeeId][idx-1]
                heapq.heappush(heap, (T, Tweet, idx-1, followeeId))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
