class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.time = 0
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        full = []
        full += self.tweets[userId]
        for f in self.following[userId]:
            full += self.tweets[f]

        full.sort(key=lambda x: (-x[0]))

        full = [x[1] for x in full]

        return full[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
        
