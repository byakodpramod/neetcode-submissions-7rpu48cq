class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append((tweetId, self.time))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.followMap:
            self.followMap[userId] = set()
        self.followMap[userId].add(userId)
        heap = []
        res = []
        for followee in self.followMap[userId]:
            if followee in self.tweet:
                tweetId, time = self.tweet[followee][-1]
                heapq.heappush(heap, (time, tweetId, len(self.tweet[followee])-1, followee))
        while len(res) < 10 and heap:
            curTime, curTweetId, Idx, curFollowee = heapq.heappop(heap)
            res.append(curTweetId)
            if Idx > 0:
                tweetId, time = self.tweet[curFollowee][Idx-1]
                heapq.heappush(heap, (time, tweetId, Idx-1, curFollowee))
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap:
            if followeeId in self.followMap[followerId]:
                self.followMap[followerId].remove(followeeId)
