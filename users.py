from user import User


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
        pass
