import heapq
class Twitter:

    def __init__(self):

        self.twt_cnt: int = 0

        self.tweets = defaultdict(list)

        self.follosh = defaultdict(set)

        self.top_k: int = 10
        

    def postTweet(self, userId: int, tweetId: int) -> None:


        self.tweets[userId].append((self.twt_cnt, tweetId))

        self.twt_cnt+=1

        

    def getNewsFeed(self, userId: int) -> List[int]:

        feed = []

        for followee in self.follosh[userId]:

            #print(self.tweets[followee])

            feed.extend(self.tweets[followee])
        
        feed.extend(self.tweets[userId])

        return [tup[1] for tup in heapq.nlargest(self.top_k, feed, lambda x: x[0])]


        

    def follow(self, followerId: int, followeeId: int) -> None:
        


        return self.follosh[followerId].add(followeeId) if followerId != followeeId else None
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        return self.follosh[followerId].discard(followeeId) if followerId != followeeId else  None
