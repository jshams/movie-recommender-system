'''
### Create Users
- From the data we are going to create a bunch of user objects.
- These users will have an ID and they will store the movies they've rated.
- User objects can also be compared, and a similarity score is computed.
  - that metric can be decided on later
    - euclidian distance
    - cosine similarty
'''


class User:
    def __init__(self, _id):
        '''initialize a user object'''
        self._id = _id
        self.movie_ratings = {}

    def add_movie_rating(self, movie_id, rating):
        '''add a movie and its rating to self'''
        self.movie_ratings[movie_id] = rating

    def get_movie_rating(self, movie_id):
        '''get the users movie rating'''
        if movie_id not in self.movie_ratings:
            return None
        return self.movie_ratings[movie_id]

    def similarity(self, other_user, euclidian=False):
        pass
