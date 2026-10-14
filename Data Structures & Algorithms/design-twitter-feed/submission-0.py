from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []

        for user in users:
            tweets = self.tweets[user]
            if tweets:
                index = len(tweets) - 1
                time, tweetId = tweets[index]
                heapq.heappush(
                    heap, (-time, tweetId, user, index)
                )

        feed = []

        while heap and len(feed) < 10:
            neg_time, tweetId, user, index = heapq.heappop(heap)
            feed.append(tweetId)

            index -= 1
            if index >= 0:
                time, next_tweetId = self.tweets[user][index]
                heapq.heappush(
                    heap, (-time, next_tweetId, user, index)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)