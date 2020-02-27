from math import sqrt


class User:
    def __init__(self, _id):
        '''initialize a user object'''
        self._id = _id
        self.movie_ratings = {}

    def __eq__(self, other):
        return self._id == other._id

    def __ne__(self, other):
        return self._id != other._id

    def __gt__(self, other):
        return self._id > other._id

    def __ge__(self, other):
        return self._id <= other._id

    def __lt__(self, other):
        return self._id < other._id

    def __le__(self, other):
        return self._id <= other._id

    def __hash__(self):
        return hash(self._id)

    def add_movie_rating(self, movie_id, rating):
        '''add a movie and its rating to self'''
        self.movie_ratings[movie_id] = rating

    def get_movie_rating(self, movie_id):
        '''get the users movie rating'''
        if movie_id not in self.movie_ratings:
            return None
        return self.movie_ratings[movie_id]

    def similarity(self, other_user, euclidian=False):
        '''calculates the similarity between two users. returns a float
        from 0-1 indicating similarity. 1 being identical.
        Uses euclidian distance metric'''
        if not euclidian:
            return self.cosine_similarity(other_user)
        sum_squares = 0
        for movie, rating in self.movie_ratings.items():
            if movie in other_user.movie_ratings:
                other_rating = other_user.get_movie_rating(movie)
                squared_diff = (rating - other_rating) ** 2
                sum_squares += squared_diff
            else:
                sum_squares += rating ** 2
        for movie, rating in other_user.movie_ratings.items():
            if movie not in self.movie_ratings:
                sum_squares += rating ** 2
        return 1 / (sqrt(sum_squares) + 1)
