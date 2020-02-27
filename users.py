from user import User
from heapq import heappop, heappush


class Users:
    def __init__(self):
        '''stores all user objects by their ids'''
        self.users = {}

    def size(self):
        '''returns the number of users'''
        return len(self.users)

    def get_user_by_id(self, user_id):
        '''returns a user object from users dict based on its id'''
        return self.users[user_id]

    def add_user_rating(self, user_id, movie_id, rating):
        '''adds a new movie rating to a user in self.
        if the user does not exist in self, create the user and add
        the new movie and rating'''
        if user_id in self.users:
            user = self.get_user_by_id(user_id)
        else:
            user = User(user_id)
            self.users[user_id] = user
        user.add_movie_rating(movie_id, rating)

    def get_user_movie_rating(self, user_id, movie_id):
        '''returns the rating associated with the user and movie,
        None if the user DNE or if the user has never reviewed the movie'''
        if user_id not in self.users:
            return None
        user = self.get_user_by_id(user_id)
        return user.get_movie_rating(movie_id)

    def k_nearest_neighbors(self, new_user, k=10):
        '''finds the k nearest neighbors using linear search
        returns a dict of (user obj : similarity score)'''
        k_best_neighbors = []
        for user in self.users.values():
            if new_user._id == user._id:
                continue
            similarity = user.similarity(new_user)
            sim_and_user = (similarity, user)
            if len(k_best_neighbors) < k:
                heappush(k_best_neighbors, sim_and_user)
            else:
                if sim_and_user > k_best_neighbors[0]:
                    heappop(k_best_neighbors)
                    heappush(k_best_neighbors, sim_and_user)
        return dict([reversed(item) for item in k_best_neighbors])
