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

    def cosine_similarity(self, other_user):
        '''caluclates the cosine similarity between two users.
        The formula for cosine similarities between two users a and b is:
        cos(a, b) = (a•b)/(||a||*||b||)
        that is the dot product of a and b, divided by the magnitude of a
        multiplied by the magnitude of b
        '''
        dot_product = self.dot_product(other_user)
        self_mag = self.magnitude()
        other_mag = other_user.magnitude()
        return dot_product / (self_mag * other_mag)

    def magnitude(self):
        '''calculates and returns the magnitude of itself
        ||a|| = (∑ai**2)**0.5'''
        return sqrt(sum(rating**2 for rating in self.movie_ratings.values()))

    def dot_product(self, other_user):
        '''calculates and returns the dot product between self and other user
        (a•b) = ∑ai*bi'''
        dot_prod = 0
        for movie, rating in self.movie_ratings.items():
            if movie in other_user.movie_ratings:
                other_rating = other_user.get_movie_rating(movie)
                prod = rating * other_rating
                dot_prod += prod
        return dot_prod
